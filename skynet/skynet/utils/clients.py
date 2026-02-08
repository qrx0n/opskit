def clients(result):
    clients = [

    ]

    for sent, received in result:
        clients.append(
            {
                'ip': received.psrc,
                'mac': received.hwsrc
            }
        )


    return clients
