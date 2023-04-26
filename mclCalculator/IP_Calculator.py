import sys
import signal
import ipaddress


def IP_Calculator(ip_net):
    try:
        net = ipaddress.ip_network(ip_net, strict=False)
        print('IP版本号： ' + str(net.version))
        print('是否是私有地址： ' + str(net.is_private))
        print('网络号： ' + str(net.network_address))
        print('前缀长度： ' + str(net.prefixlen))
        print('子网掩码： ' + str(net.netmask))
        print('反子网掩码： ' + str(net.hostmask))
        print('IP地址总数: ' + str(net.num_addresses))
        print('可用IP地址总数： ' + str(len([x for x in net.hosts()])))
        print('起始可用IP地址： ' + str([x for x in net.hosts()][0]))
        print('最后可用IP地址： ' + str([x for x in net.hosts()][-1]))
        print('可用IP地址范围： ' + str([x for x in net.hosts()]
              [0]) + ' ~ ' + str([x for x in net.hosts()][-1]))
        print('广播地址： ' + str(net.broadcast_address))
    except ValueError:
        print('您输入格式有误，请检查！\n')


def quit(signum, frame):
    print("\nBye!")
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, quit)
    print("""Welcome!\nCTRL+C退出程序\n输入地址格式: IP地址/掩码; 输入样例如下: \n192.168.1.0/24或192.168.1.0/255.255.255.0\n""")
    while True:
        ip_net = input("请输入: ").replace(" ", "")
        print("****************************************************")
        IP_Calculator(ip_net)
        print("****************************************************\n")
