from colorama import Fore;
from src.banner import BANNER;

from argparse import ArgumentParser;

from requests import ConnectionError, get;



class Sub:
    def __init__(
        self, domain,
        subdomain_conf):

        self.target = domain;
        self.subdomains_conf = subdomain_conf;


    def read_config(
        self, conf_path):
        conf_file = open(
            conf_path);
        
        content = conf_file.read(
            );

        del conf_file;

        return content.splitlines(
            ); 


    def save_data(
        self, output, 
        domain):
        
        with open(\
            f'''subdomains_{domain.split(
                ".")[0]}.txt''', 'w') as temp:
            for subdomain in output:
                temp.write(
                    f'{subdomain}\n');
                del subdomain;


    def perf(
        self, subdomains,
        main_domain):
        discovered_ = [

        ];

        for subdomain in subdomains:
            target = f"http://{subdomain}.{main_domain}";

            try: 
                get(
                    target);

            except ConnectionError:
                continue;

            else: 
                print(
                    f"{Fore.LIGHTCYAN_EX}[*] Discovered subdomain : \
                    `{target}`;");
            
            discovered_.append(
                target);

            del subdomain, target;

        self.save_data(
            discovered_, main_domain);


def argparser():
    parser = ArgumentParser(
        prog='SUBB3R',
        description="subb3r - a powerful subdomain scanner.");

    parser.add_argument(
        '-d', '--domain');
    parser.add_argument(
        '-f', '--subdomains');

    return parser.parse_args();


def banner(banner):
    print(Fore.LIGHTGREEN_EX + banner);
    print('--------------------------------------------------\n')


def main():
    args = argparser(
        );

    banner(
        BANNER);

    exec_ = Sub(
        args.domain, args.subdomains);
    
    conf = exec_.read_config(
        exec_.subdomains_conf);
    
    exec_.perf(
        conf, exec_.target);


if __name__ == '__main__':
    main(
        );
