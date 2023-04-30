import sys
import ipaddress
import dns.message
import dns.edns
import dns.query
import dns.rdatatype
import dns.resolver

def check_ecs_support(domain, dns_server, client_subnet):
    try:
        # 創建一個 DNS 查詢訊息
        query = dns.message.make_query(domain, dns.rdatatype.A)
        print(f"正在查詢 {domain} 的 A 記錄...")

        # 將客戶端子網解析為 IP 位址和前綴長度
        client_ip, prefix_length = client_subnet.split('/')
        prefix_length = int(prefix_length)

        # 設定 EDNS0 選項以支持 ECS
        print("正在設定 EDNS0 選項以支持 ECS...")
        ecs_option = dns.edns.ECSOption(client_ip, prefix_length, 0)
        query.use_edns(options=[ecs_option])
        print("正在設定 EDNS0 選項以支持 ECS...OK")

        # 向指定的 DNS 伺服器發送查詢
        print(f"正在向 DNS 伺服器 {dns_server} 發送查詢...")
        response = dns.query.udp(query, dns_server)

        # 檢查回應中是否包含 ECS 選項
        ecs_supported = any(isinstance(option, dns.edns.ECSOption) for option in response.options)

        if ecs_supported:
            print("DNS 伺服器支持 ECS。")
        else:
            print("DNS 伺服器不支持 ECS。")

    except Exception as e:
        print(f"查詢過程中出現錯誤: {e}")

if __name__ == "__main__":
    domain = "cdn-niu-cdrs01.tanetcdn.edu.tw" if len(sys.argv) < 2 else sys.argv[1]
    dns_server = "8.8.8.8" if len(sys.argv) < 3 else sys.argv[2]
    client_subnet = "59.124.220.95/24" if len(sys.argv) < 4 else sys.argv[3]


    print("ECS Protocol Checker, (c)Digital Explorer Technology 2019-")

    check_ecs_support(domain, dns_server, client_subnet)
