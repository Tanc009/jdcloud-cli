# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.

from argparse import RawTextHelpFormatter
from jdcloud_cli.cement.ext.ext_argparse import expose
from jdcloud_cli.controllers.base_controller import BaseController
from jdcloud_cli.client_factory import ClientFactory
from jdcloud_cli.parameter_builder import collect_user_args, collect_user_headers
from jdcloud_cli.printer import Printer
from jdcloud_cli.skeleton import Skeleton


class BaseantiController(BaseController):
    class Meta:
        label = 'baseanti'
        help = 'Anti-DDoS Basic APIs'
        description = '''
        baseanti cli 子命令，DDoS 基础防护防护 IP、攻击记录相关接口。
        OpenAPI文档地址为：https://docs.jdcloud.com/cn/anti-ddos-basic/api/overview
        '''
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--page-number'], dict(help="""(int) 页码 """, dest='pageNumber', type=int, required=False)),
            (['--page-size'], dict(help="""(int) 分页大小 """, dest='pageSize', type=int, required=False)),
            (['--start-time'], dict(help="""(string) 开始时间, UTC 时间, 格式: yyyy-MM-dd'T'HH:mm:ssZ """, dest='startTime',  required=True)),
            (['--end-time'], dict(help="""(string) 结束时间, UTC 时间, 格式: yyyy-MM-dd'T'HH:mm:ssZ """, dest='endTime',  required=True)),
            (['--ip'], dict(help="""(array: string) 基础防护已防护的公网 IP, ip 不为空时, 查询 ip 对应的攻击记录, ip 为空时, 查询用户所有攻击记录; - 使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describeelasticipresources">describeElasticIpResources</a> 接口查询基础防护已防护的私有网络弹性公网 IP; - 使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describecpsipresources">describeCpsIpResources</a> 接口查询基础防护已防护的云物理服务器公网IP 和 弹性公网 IP;  """, dest='ip',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询攻击记录 ''',
        description='''
            查询攻击记录。

            示例: jdc baseanti describe-attack-logs  --start-time xxx --end-time xxx
        ''',
    )
    def describe_attack_logs(self):
        client_factory = ClientFactory('baseanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.baseanti.apis.DescribeAttackLogsRequest import DescribeAttackLogsRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeAttackLogsRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--start-time'], dict(help="""(string) 开始时间, UTC 时间, 格式: yyyy-MM-dd'T'HH:mm:ssZ """, dest='startTime',  required=True)),
            (['--end-time'], dict(help="""(string) 结束时间, UTC 时间, 格式: yyyy-MM-dd'T'HH:mm:ssZ """, dest='endTime',  required=True)),
            (['--ip'], dict(help="""(array: string) 基础防护已防护的公网 IP, ip 不为空时, 统计 ip 对应的攻击情况, ip 为空时, 统计用户所有公网 IP 的攻击情况; - 使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describeelasticipresources">describeElasticIpResources</a> 接口查询基础防护已防护的私有网络弹性公网 IP; - 使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describecpsipresources">describeCpsIpResources</a> 接口查询基础防护已防护的云物理服务器公网IP 和 弹性公网 IP;  """, dest='ip',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 攻击情况统计 ''',
        description='''
            攻击情况统计。

            示例: jdc baseanti describe-attack-statistics  --start-time xxx --end-time xxx
        ''',
    )
    def describe_attack_statistics(self):
        client_factory = ClientFactory('baseanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.baseanti.apis.DescribeAttackStatisticsRequest import DescribeAttackStatisticsRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeAttackStatisticsRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--start-time'], dict(help="""(string) 开始时间, UTC 时间, 格式: yyyy-MM-dd'T'HH:mm:ssZ """, dest='startTime',  required=True)),
            (['--end-time'], dict(help="""(string) 结束时间, UTC 时间, 格式: yyyy-MM-dd'T'HH:mm:ssZ """, dest='endTime',  required=True)),
            (['--ip'], dict(help="""(array: string) 基础防护已防护的公网 IP, ip 不为空时, 查询 ip 对应的各类型攻击次数, ip 为空时, 查询用户所有公网 IP 的各类型攻击次数; - 使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describeelasticipresources">describeElasticIpResources</a> 接口查询基础防护已防护的私有网络弹性公网 IP; - 使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describecpsipresources">describeCpsIpResources</a> 接口查询基础防护已防护的云物理服务器公网IP 和 弹性公网 IP;  """, dest='ip',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询各类型攻击次数 ''',
        description='''
            查询各类型攻击次数。

            示例: jdc baseanti describe-attack-type-count  --start-time xxx --end-time xxx
        ''',
    )
    def describe_attack_type_count(self):
        client_factory = ClientFactory('baseanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.baseanti.apis.DescribeAttackTypeCountRequest import DescribeAttackTypeCountRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeAttackTypeCountRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--start-time'], dict(help="""(string) 开始时间, UTC 时间, 格式: yyyy-MM-dd'T'HH:mm:ssZ """, dest='startTime',  required=True)),
            (['--end-time'], dict(help="""(string) 结束时间, UTC 时间, 格式: yyyy-MM-dd'T'HH:mm:ssZ """, dest='endTime',  required=True)),
            (['--ip'], dict(help="""(array: string) 基础防护已防护的公网 IP; - 使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describeelasticipresources">describeElasticIpResources</a> 接口查询基础防护已防护的私有网络弹性公网 IP; - 使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describecpsipresources">describeCpsIpResources</a> 接口查询基础防护已防护的云物理服务器公网IP 和 弹性公网 IP;  """, dest='ip',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询多个公网 IP 的监控流量, 支持 ipv4 和 ipv6 ''',
        description='''
            查询多个公网 IP 的监控流量, 支持 ipv4 和 ipv6。

            示例: jdc baseanti describe-ip-monitor-flow  --start-time xxx --end-time xxx
        ''',
    )
    def describe_ip_monitor_flow(self):
        client_factory = ClientFactory('baseanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.baseanti.apis.DescribeIpMonitorFlowRequest import DescribeIpMonitorFlowRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeIpMonitorFlowRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域编码. 基础防护已支持华北-北京, 华东-宿迁, 华东-上海, 华南-广州;  """, dest='regionId',  required=False)),
            (['--ip'], dict(help="""(string) IP 模糊匹配 """, dest='ip',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询公网 IP 的安全信息列表. 包括私有网络的弹性公网 IP(运营商级 NAT 保留地址除外), 云物理服务器的公网 IP 和弹性公网 IP. (已废弃, 建议使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describeelasticipresources">describeElasticIpResources</a>, <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describecpsipresources">describeCpsIpResources</a> 接口)";  ''',
        description='''
            查询公网 IP 的安全信息列表. 包括私有网络的弹性公网 IP(运营商级 NAT 保留地址除外), 云物理服务器的公网 IP 和弹性公网 IP. (已废弃, 建议使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describeelasticipresources">describeElasticIpResources</a>, <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describecpsipresources">describeCpsIpResources</a> 接口)"; 。

            示例: jdc baseanti describe-ip-resources 
        ''',
    )
    def describe_ip_resources(self):
        client_factory = ClientFactory('baseanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.baseanti.apis.DescribeIpResourcesRequest import DescribeIpResourcesRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeIpResourcesRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域编码. 基础防护已支持华北-北京, 华东-宿迁, 华东-上海, 华南-广州;  """, dest='regionId',  required=False)),
            (['--page-number'], dict(help="""(int) 页码 """, dest='pageNumber', type=int, required=False)),
            (['--page-size'], dict(help="""(int) 分页大小 """, dest='pageSize', type=int, required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询私有网络的弹性公网 IP 的安全信息. 包括私有网络的弹性公网 IP(运营商级 NAT 保留地址除外);  ''',
        description='''
            查询私有网络的弹性公网 IP 的安全信息. 包括私有网络的弹性公网 IP(运营商级 NAT 保留地址除外); 。

            示例: jdc baseanti describe-elastic-ip-resources 
        ''',
    )
    def describe_elastic_ip_resources(self):
        client_factory = ClientFactory('baseanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.baseanti.apis.DescribeElasticIpResourcesRequest import DescribeElasticIpResourcesRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeElasticIpResourcesRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域编码. 基础防护已支持华北-北京, 华东-宿迁, 华东-上海, 华南-广州;  """, dest='regionId',  required=False)),
            (['--page-number'], dict(help="""(int) 页码 """, dest='pageNumber', type=int, required=False)),
            (['--page-size'], dict(help="""(int) 分页大小 """, dest='pageSize', type=int, required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询云物理服务器公网 IP 的安全信息. 包括云物理服务器的公网 IP 和弹性公网 IP.;  ''',
        description='''
            查询云物理服务器公网 IP 的安全信息. 包括云物理服务器的公网 IP 和弹性公网 IP.; 。

            示例: jdc baseanti describe-cps-ip-resources 
        ''',
    )
    def describe_cps_ip_resources(self):
        client_factory = ClientFactory('baseanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.baseanti.apis.DescribeCpsIpResourcesRequest import DescribeCpsIpResourcesRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeCpsIpResourcesRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域编码. 基础防护已支持华北-北京, 华东-宿迁, 华东-上海, 华南-广州;  """, dest='regionId',  required=False)),
            (['--ip'], dict(help="""(string) 基础防护已防护的公网 IP, 仅支持 ipv4 格式; - 使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describeelasticipresources">describeElasticIpResources</a> 接口查询基础防护已防护的私有网络弹性公网 IP; - 使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describecpsipresources">describeCpsIpResources</a> 接口查询基础防护已防护的云物理服务器公网IP 和 弹性公网 IP;  """, dest='ip',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询公网 IP 安全信息, 仅支持 ipv4. (已废弃, 建议使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describeipsafetyinfo">describeIpSafetyInfo</a> 接口);  ''',
        description='''
            查询公网 IP 安全信息, 仅支持 ipv4. (已废弃, 建议使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describeipsafetyinfo">describeIpSafetyInfo</a> 接口); 。

            示例: jdc baseanti describe-ip-resource-info  --ip xxx
        ''',
    )
    def describe_ip_resource_info(self):
        client_factory = ClientFactory('baseanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.baseanti.apis.DescribeIpResourceInfoRequest import DescribeIpResourceInfoRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeIpResourceInfoRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域编码. 基础防护已支持华北-北京, 华东-宿迁, 华东-上海, 华南-广州;  """, dest='regionId',  required=False)),
            (['--ip'], dict(help="""(string) 基础防护已防护公网 IP.; - 使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describeelasticipresources">describeElasticIpResources</a> 接口查询基础防护已防护的私有网络弹性公网 IP; - 使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describecpsipresources">describeCpsIpResources</a> 接口查询基础防护已防护的云物理服务器公网IP 和 弹性公网 IP;  """, dest='ip',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询基础防护已防护公网 IP 安全信息, 支持 ipv4 和 ipv6 ''',
        description='''
            查询基础防护已防护公网 IP 安全信息, 支持 ipv4 和 ipv6。

            示例: jdc baseanti describe-ip-safety-info  --ip xxx
        ''',
    )
    def describe_ip_safety_info(self):
        client_factory = ClientFactory('baseanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.baseanti.apis.DescribeIpSafetyInfoRequest import DescribeIpSafetyInfoRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeIpSafetyInfoRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域编码. 基础防护已支持华北-北京, 华东-宿迁, 华东-上海, 华南-广州;  """, dest='regionId',  required=False)),
            (['--ip'], dict(help="""(string) 基础防护已防护的公网 IP, 仅支持 ipv4 格式; - 使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describeelasticipresources">describeElasticIpResources</a> 接口查询基础防护已防护的私有网络弹性公网 IP; - 使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describecpsipresources">describeCpsIpResources</a> 接口查询基础防护已防护的云物理服务器公网IP 和 弹性公网 IP;  """, dest='ip',  required=True)),
            (['--clean-threshold-spec'], dict(help="""(cleanThresholdSpec) 请求参数 """, dest='cleanThresholdSpec',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 设置基础防护已防护公网 IP 的清洗阈值, 仅支持 ipv4. (已废弃, 建议使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/setipcleanthreshold">setIpCleanThreshold</a> 接口);  ''',
        description='''
            设置基础防护已防护公网 IP 的清洗阈值, 仅支持 ipv4. (已废弃, 建议使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/setipcleanthreshold">setIpCleanThreshold</a> 接口); 。

            示例: jdc baseanti set-clean-threshold  --ip xxx --clean-threshold-spec '{"":""}'
        ''',
    )
    def set_clean_threshold(self):
        client_factory = ClientFactory('baseanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.baseanti.apis.SetCleanThresholdRequest import SetCleanThresholdRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = SetCleanThresholdRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域编码. 基础防护已支持华北-北京, 华东-宿迁, 华东-上海, 华南-广州;  """, dest='regionId',  required=False)),
            (['--ip-clean-threshold-spec'], dict(help="""(ipCleanThresholdSpec) 请求参数 """, dest='ipCleanThresholdSpec',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 设置基础防护已防护公网 IP 的清洗阈值, 支持 ipv4 和 ipv6 ''',
        description='''
            设置基础防护已防护公网 IP 的清洗阈值, 支持 ipv4 和 ipv6。

            示例: jdc baseanti set-ip-clean-threshold  --ip-clean-threshold-spec '{"":""}'
        ''',
    )
    def set_ip_clean_threshold(self):
        client_factory = ClientFactory('baseanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.baseanti.apis.SetIpCleanThresholdRequest import SetIpCleanThresholdRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = SetIpCleanThresholdRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域编码. 基础防护已支持华北-北京, 华东-宿迁, 华东-上海, 华南-广州;  """, dest='regionId',  required=False)),
            (['--ip'], dict(help="""(string) 基础防护已防护公网 IP.; - 使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describeelasticipresources">describeElasticIpResources</a> 接口查询基础防护已防护的私有网络弹性公网 IP; - 使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describecpsipresources">describeCpsIpResources</a> 接口查询基础防护已防护的云物理服务器公网IP 和 弹性公网 IP;  """, dest='ip',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询公网 IP 可设置清洗阈值范围, 支持 ipv4 和 ipv6 ''',
        description='''
            查询公网 IP 可设置清洗阈值范围, 支持 ipv4 和 ipv6。

            示例: jdc baseanti describe-ip-clean-threshold-range  --ip xxx
        ''',
    )
    def describe_ip_clean_threshold_range(self):
        client_factory = ClientFactory('baseanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.baseanti.apis.DescribeIpCleanThresholdRangeRequest import DescribeIpCleanThresholdRangeRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeIpCleanThresholdRangeRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域编码. 基础防护已支持华北-北京, 华东-宿迁, 华东-上海, 华南-广州;  """, dest='regionId',  required=False)),
            (['--ip'], dict(help="""(string) 基础防护已防护的公网 IP, 仅支持 ipv4 格式; - 使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describeelasticipresources">describeElasticIpResources</a> 接口查询基础防护已防护的私有网络弹性公网 IP; - 使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describecpsipresources">describeCpsIpResources</a> 接口查询基础防护已防护的云物理服务器公网IP 和 弹性公网 IP;  """, dest='ip',  required=True)),
            (['--start'], dict(help="""(int) 限制查询的开始范围 """, dest='start', type=int, required=False)),
            (['--limit'], dict(help="""(int) 限制查询的记录数 """, dest='limit', type=int, required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询公网 IP 的攻击记录, 仅支持 ipv4. (已废弃, 建议使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describeattacklogs">describeAttackLogs</a> 接口);  ''',
        description='''
            查询公网 IP 的攻击记录, 仅支持 ipv4. (已废弃, 建议使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describeattacklogs">describeAttackLogs</a> 接口); 。

            示例: jdc baseanti describe-ip-resource-protect-info  --ip xxx
        ''',
    )
    def describe_ip_resource_protect_info(self):
        client_factory = ClientFactory('baseanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.baseanti.apis.DescribeIpResourceProtectInfoRequest import DescribeIpResourceProtectInfoRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeIpResourceProtectInfoRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域编码. 基础防护已支持华北-北京, 华东-宿迁, 华东-上海, 华南-广州;  """, dest='regionId',  required=False)),
            (['--ip'], dict(help="""(string) 基础防护已防护的公网 IP, 仅支持 ipv4 格式; - 使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describeelasticipresources">describeElasticIpResources</a> 接口查询基础防护已防护的私有网络弹性公网 IP; - 使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describecpsipresources">describeCpsIpResources</a> 接口查询基础防护已防护的云物理服务器公网IP 和 弹性公网 IP;  """, dest='ip',  required=True)),
            (['--end-time'], dict(help="""(string) 查询的结束时间, UTC时间, 格式: yyyy-MM-dd'T'HH:mm:ssZ, 为空时查询当前时间之前 15 分钟内监控流量 """, dest='endTime',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询公网 IP 的 endTime 之前 15 分钟内监控流量, 仅支持 ipv4. (已废弃, 建议使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describeipmonitorflow">describeIpMonitorFlow</a> 接口);  ''',
        description='''
            查询公网 IP 的 endTime 之前 15 分钟内监控流量, 仅支持 ipv4. (已废弃, 建议使用 <a href="http://docs.jdcloud.com/anti-ddos-basic/api/describeipmonitorflow">describeIpMonitorFlow</a> 接口); 。

            示例: jdc baseanti describe-ip-resource-flow  --ip xxx
        ''',
    )
    def describe_ip_resource_flow(self):
        client_factory = ClientFactory('baseanti')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.baseanti.apis.DescribeIpResourceFlowRequest import DescribeIpResourceFlowRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeIpResourceFlowRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--api'], dict(help="""(string) api name """, choices=['describe-attack-logs','describe-attack-statistics','describe-attack-type-count','describe-ip-monitor-flow','describe-ip-resources','describe-elastic-ip-resources','describe-cps-ip-resources','describe-ip-resource-info','describe-ip-safety-info','set-clean-threshold','set-ip-clean-threshold','describe-ip-clean-threshold-range','describe-ip-resource-protect-info','describe-ip-resource-flow',], required=True)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 生成单个API接口的json骨架空字符串 ''',
        description='''
            生成单个API接口的json骨架空字符串。

            示例: jdc nc generate-skeleton --api describeContainer ''',
    )
    def generate_skeleton(self):
        skeleton = Skeleton('baseanti', self.app.pargs.api)
        skeleton.show()
