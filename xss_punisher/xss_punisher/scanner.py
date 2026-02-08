from argparse import ArgumentParser;

from pprint import pprint;
from colorama import Fore;
from src.banner import PUNISHER_TEXT, XSS_TEXT, BANNER; 

from urllib.parse import urljoin;

from requests import post, get;
from bs4 import BeautifulSoup as BSoup;



class XSS:
    def __init__(
        self, target, 
        test_payload):

        self.target = target;
        self.payload = test_payload;


    def show_banner(
        self, banner, 
        text_list):
        print(
            Fore.LIGHTRED_EX + banner);
        print(
            Fore.YELLOW + text_list[0]);
        print(
            Fore.YELLOW + text_list[1]);

    
    def init_soup(
        self, target,
        ptype):
        return BSoup(
            get(
            target).content, 
            ptype);


    def get_all_forms(
        self, soup):
        return soup.find_all(
            'form');


    def get_details(
        self, form):
        
        details = {
            
        };

        action = form.attrs.get(
            'action', 
            '').lower();
        
        method = form.attrs.get(
            'method', 
            'get').lower();

        inputs = [
        
        ];

        for tag in form.find_all('input'):
            type = tag.attrs.get(
                'type', 
                'text');

            name = tag.attrs.get(
                'name');

            inputs.append(
                {
                    "type": type,
                    "name": name,
                });

        details["action"] = action;
        details["method"] = method;
        details["inputs"] = inputs;

        del action, method, inputs;
        return details;

    
    def submit_form(
        self, details,
        target, payload):

        targetU = urljoin(
            target,
            details["action"]);


        inputs = details["inputs"];

        data = {

        };

        for input in inputs:
            if (input["type"] == "text"
                or input["type"] == "search"):
                input["value"] = payload;

            name = input.get("name");
            value = input.get("value");

            if (name 
                and value):
                data[name] = value;
        
            del value, name;

        del inputs;

        print(
            f"\n{Fore.LIGHTBLUE_EX}[*] Submitting malicious payload to : {Fore.WHITE}'{Fore.CYAN + targetU}{Fore.WHITE}'");
        
        print(
            f"{Fore.LIGHTBLUE_EX}[*] Data: {Fore.WHITE}'{Fore.CYAN + str(data)}{Fore.WHITE}'");

        if (details["method"] == "post"):
            return post(
                targetU, 
                data=data);

        else:
            return get(
                targetU,
                params=data);


    def scan(
        self, target,
        payload):

        self.show_banner(
        BANNER, 
        [
        XSS_TEXT, 
        PUNISHER_TEXT,
        ]);

        soup = self.init_soup(
            target,
            'html.parser');

        forms = self.get_all_forms(
            soup);

        print(
            f"\n{Fore.GREEN}[*] Detected {len(forms)} forms on {target}");

        is_vulnerable = False;

        for form in forms:
            details = self.get_details(
                form);

            content = self.submit_form(
                details,
                target, payload).content.decode();

            if (payload in content):
                print(
                    f"\n{Fore.LIGHTBLUE_EX}[!] XSS Detected on : {Fore.WHITE}'{Fore.CYAN + target}{Fore.WHITE}'");

                print(
                    f"\n[*] Form details:");

                pprint(details);
                is_vulnerable = True; 

        if (is_vulnerable):
            print(
                f"\n{Fore.RED}[!] XSS Vulnerability Discovered on : {target}");

        else:
            print(
                f"\n{Fore.GREEN}[+] The site is secure!");


def argument_parser():
    parser = ArgumentParser(
        prog='scanner.py',
        epilog='You have to set target and payload, to start punishing the NET.');

    parser.add_argument(
        '-t', '--target',
        help='set target (web-site, web-application)');
    parser.add_argument(
        '-p', '--payload',
        help='set payload in ""');
    parser.add_argument(
        '-v', '--verbose');

    return parser.parse_args();

def main():
    args = argument_parser();

    exec_ = XSS(
        args.target,
        args.payload);
    
    exec_.scan(
        exec_.target,
        exec_.payload);

    print(Fore.RESET + "\r");


if __name__ == "__main__":
    main();
