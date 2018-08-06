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
from cement.ext.ext_argparse import expose
from jdcloud_cli.controllers.base_controller import BaseController
from jdcloud_cli.client_factory import ClientFactory
from jdcloud_cli.parameter_builder import collect_user_args, collect_user_headers
from jdcloud_cli.printer import Printer
from jdcloud_cli.skeleton import Skeleton


class MonitorController(BaseController):
    class Meta:
        label = 'monitor'
        help = '使用该子命令操作monitor相关资源'
        description = '''
        monitor cli 子命令，可以使用该子命令操作monitor相关资源。
        OpenAPI文档地址为：https://www.jdcloud.com/help/detail/380/isCatalog/0
        '''
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域 Id """, dest='regionId', required=False)),
            (['--service-code'], dict(help="""(string) 产品名称 """, dest='serviceCode', required=False)),
            (['--resource-id'], dict(help="""(string) 资源Id """, dest='resourceId', required=False)),
            (['--status'], dict(help="""(int) 规则报警状态, 1：正常, 2：报警，4：数据不足 """, dest='status', required=False)),
            (['--is-alarming'], dict(help="""(int) 是否为正在报警的规则，0为忽略，1为是，与 status 同时只能生效一个,isAlarming 优先生效 """, dest='isAlarming', required=False)),
            (['--enabled'], dict(help="""(int) 规则状态：1为启用，0为禁用 """, dest='enabled', required=False)),
            (['--page-number'], dict(help="""(int) 页码, 默认为1, 取值范围：[1,∞) """, dest='pageNumber', required=False)),
            (['--page-size'], dict(help="""(int) 分页大小，默认为20，取值范围：[10,100] """, dest='pageSize', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询监控规则 ''',
        description='''
            查询监控规则。

            示例: jdc monitor describe-alarms 
        ''',
    )
    def describe_alarms(self):
        client_factory = ClientFactory('monitor')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.monitor.apis.DescribeAlarmsRequest import DescribeAlarmsRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeAlarmsRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域 Id """, dest='regionId', required=False)),
            (['--client-token'], dict(help="""(string) 幂等性校验参数，最长32位，值不变则返回值不会变 """, dest='clientToken', required=True)),
            (['--create-alarm-spec'], dict(help="""(createAlarmSpec) NA """, dest='createAlarmSpec', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 创建报警规则，可以为某一个实例创建报警规则，也可以为多个实例同时创建报警规则。 ''',
        description='''
            创建报警规则，可以为某一个实例创建报警规则，也可以为多个实例同时创建报警规则。。

            示例: jdc monitor create-alarm  --client-token xxx --create-alarm-spec {"":""}
        ''',
    )
    def create_alarm(self):
        client_factory = ClientFactory('monitor')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.monitor.apis.CreateAlarmRequest import CreateAlarmRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = CreateAlarmRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域 Id """, dest='regionId', required=False)),
            (['--ids'], dict(help="""(string) 待删除的规则id，用"|"间隔 """, dest='ids', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 批量删除已创建的报警规则 ''',
        description='''
            批量删除已创建的报警规则。

            示例: jdc monitor delete-alarms  --ids xxx
        ''',
    )
    def delete_alarms(self):
        client_factory = ClientFactory('monitor')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.monitor.apis.DeleteAlarmsRequest import DeleteAlarmsRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DeleteAlarmsRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域 Id """, dest='regionId', required=False)),
            (['--alarm-id'], dict(help="""(string) 规则id """, dest='alarmId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询规则详情 ''',
        description='''
            查询规则详情。

            示例: jdc monitor describe-alarms-by-id  --alarm-id xxx
        ''',
    )
    def describe_alarms_by_id(self):
        client_factory = ClientFactory('monitor')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.monitor.apis.DescribeAlarmsByIDRequest import DescribeAlarmsByIDRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeAlarmsByIDRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域 Id """, dest='regionId', required=False)),
            (['--alarm-id'], dict(help="""(string) 规则id """, dest='alarmId', required=True)),
            (['--calculation'], dict(help="""(string) 统计方法：平均值=avg、最大值=max、最小值=min、总和=sum """, dest='calculation', required=True)),
            (['--contact-groups'], dict(help="""(array: string) 通知的联系组，如 [“联系组1”,”联系组2”] """, dest='contactGroups', required=False)),
            (['--contact-persons'], dict(help="""(array: string) 通知的联系人，如 [“联系人1”,”联系人2”] """, dest='contactPersons', required=False)),
            (['--down-sample'], dict(help="""(string) 取样频次 """, dest='downSample', required=False)),
            (['--metric'], dict(help="""(string) 根据产品线查询可用监控项列表 接口 返回的Metric字段 """, dest='metric', required=True)),
            (['--notice-period'], dict(help="""(int) 通知周期 单位：小时 """, dest='noticePeriod', required=False)),
            (['--operation'], dict(help="""(string) >=、>、<、<=、==、!= """, dest='operation', required=True)),
            (['--period'], dict(help="""(int) 统计周期（单位：分钟），可选值：2,5,15,30,60 """, dest='period', required=True)),
            (['--service-code'], dict(help="""(string) 产品名称 """, dest='serviceCode', required=True)),
            (['--threshold'], dict(help="""(float) 阈值 """, dest='threshold', required=True)),
            (['--times'], dict(help="""(int) 连续多少次后报警，可选值:1,2,3,5 """, dest='times', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 修改已创建的报警规则 ''',
        description='''
            修改已创建的报警规则。

            示例: jdc monitor update-alarm  --alarm-id xxx --calculation xxx --metric xxx --operation xxx --period 0 --service-code xxx --threshold  --times 0
        ''',
    )
    def update_alarm(self):
        client_factory = ClientFactory('monitor')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.monitor.apis.UpdateAlarmRequest import UpdateAlarmRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = UpdateAlarmRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域 Id """, dest='regionId', required=False)),
            (['--alarm-id'], dict(help="""(string) 规则id """, dest='alarmId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 启用报警规则，当客户的报警规则处于停止状态时，可以使用此接口启用报警规则。 ''',
        description='''
            启用报警规则，当客户的报警规则处于停止状态时，可以使用此接口启用报警规则。。

            示例: jdc monitor enable-alarm  --alarm-id xxx
        ''',
    )
    def enable_alarm(self):
        client_factory = ClientFactory('monitor')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.monitor.apis.EnableAlarmRequest import EnableAlarmRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = EnableAlarmRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域 Id """, dest='regionId', required=False)),
            (['--alarm-id'], dict(help="""(string) 规则id """, dest='alarmId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 禁用报警规则。报警规则禁用后，将停止探测实例的监控项数据。 ''',
        description='''
            禁用报警规则。报警规则禁用后，将停止探测实例的监控项数据。。

            示例: jdc monitor disable-alarm  --alarm-id xxx
        ''',
    )
    def disable_alarm(self):
        client_factory = ClientFactory('monitor')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.monitor.apis.DisableAlarmRequest import DisableAlarmRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DisableAlarmRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域 Id """, dest='regionId', required=False)),
            (['--id'], dict(help="""(string) 报警规则的Id """, dest='id', required=False)),
            (['--service-code'], dict(help="""(string) 产品名称 """, dest='serviceCode', required=False)),
            (['--resource-id'], dict(help="""(string) 资源Id """, dest='resourceId', required=False)),
            (['--start-time'], dict(help="""(string) 查询数据开始时间，默认24小时前，可以输入long型时间，也可以输入yyyy-MM-dd'T'HH:mm:ssZ类型时间 """, dest='startTime', required=True)),
            (['--end-time'], dict(help="""(string) 查询数据结束时间，默认当前时间，可以输入long型时间，也可以输入yyyy-MM-dd'T'HH:mm:ssZ类型时间 """, dest='endTime', required=True)),
            (['--page-number'], dict(help="""(int) 页码, 默认为1, 取值范围：[1,∞) """, dest='pageNumber', required=False)),
            (['--page-size'], dict(help="""(int) 分页大小，默认为20，取值范围：[10,100] """, dest='pageSize', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询报警历史 ''',
        description='''
            查询报警历史。

            示例: jdc monitor describe-alarm-history  --start-time xxx --end-time xxx
        ''',
    )
    def describe_alarm_history(self):
        client_factory = ClientFactory('monitor')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.monitor.apis.DescribeAlarmHistoryRequest import DescribeAlarmHistoryRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeAlarmHistoryRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--service-code'], dict(help="""(string) 资源的类型 ： ; vm-->云主机; disk-->云硬盘; ip-->公网ip; balance-->负载均衡; database-->云数据库mysql版本; cdn-->京东CDN; redis-->redis云缓存; mongodb-->mongoDB云缓存; storage-->云存储; sqlserver-->云数据库sqlserver版 ; nativecontainer-->容器;  """, dest='serviceCode', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 根据产品线查询可用监控项列表 ''',
        description='''
            根据产品线查询可用监控项列表。

            示例: jdc monitor describe-metrics  --service-code xxx
        ''',
    )
    def describe_metrics(self):
        client_factory = ClientFactory('monitor')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.monitor.apis.DescribeMetricsRequest import DescribeMetricsRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeMetricsRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--service-code'], dict(help="""(string) 资源的类型，默认为空，展示所有项目; vm-->云主机; disk-->云硬盘; ip-->公网ip; balance-->负载均衡; database-->云数据库mysql版本; cdn-->京东CDN; redis-->redis云缓存; mongodb-->mongoDB云缓存; storage-->云存储; sqlserver-->云数据库sqlserver版 ; nativecontainer-->容器;  """, dest='serviceCode', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询可用创建监控规则的指标列表 ''',
        description='''
            查询可用创建监控规则的指标列表。

            示例: jdc monitor describe-metrics-for-create-alarm 
        ''',
    )
    def describe_metrics_for_create_alarm(self):
        client_factory = ClientFactory('monitor')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.monitor.apis.DescribeMetricsForCreateAlarmRequest import DescribeMetricsForCreateAlarmRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeMetricsForCreateAlarmRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域 Id """, dest='regionId', required=False)),
            (['--metric'], dict(help="""(string) 监控项英文标识(id) """, dest='metric', required=True)),
            (['--service-code'], dict(help="""(string) 资源的类型，取值vm, lb, ip, database 等 """, dest='serviceCode', required=True)),
            (['--resource-id'], dict(help="""(string) 资源的uuid """, dest='resourceId', required=True)),
            (['--start-time'], dict(help="""(string) 查询时间范围的开始时间， UTC时间，格式：yyyy-MM-dd'T'HH:mm:ssZ（默认为当前时间，早于30d时，将被重置为30d） """, dest='startTime', required=False)),
            (['--end-time'], dict(help="""(string) 查询时间范围的结束时间， UTC时间，格式：2016-12- yyyy-MM-dd'T'HH:mm:ssZ（为空时，将由startTime与timeInterval计算得出） """, dest='endTime', required=False)),
            (['--time-interval'], dict(help="""(string) 时间间隔：1h，6h，12h，1d，3d，7d，14d，固定时间间隔，timeInterval 与 endTime 至少填一项 """, dest='timeInterval', required=False)),
            (['--tags'], dict(help="""(array: tagFilter) 自定义标签 """, dest='tags', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查看某资源的监控数据 ''',
        description='''
            查看某资源的监控数据。

            示例: jdc monitor describe-metric-data  --metric xxx --service-code xxx --resource-id xxx
        ''',
    )
    def describe_metric_data(self):
        client_factory = ClientFactory('monitor')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.monitor.apis.DescribeMetricDataRequest import DescribeMetricDataRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeMetricDataRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--metric-data-list'], dict(help="""(array: metricDataCm) 数据参数 """, dest='metricDataList', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 自定义监控数据上报接口 ''',
        description='''
            自定义监控数据上报接口。

            示例: jdc monitor put-metric-data 
        ''',
    )
    def put_metric_data(self):
        client_factory = ClientFactory('monitor')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.monitor.apis.PutMetricDataRequest import PutMetricDataRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = PutMetricDataRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--api'], dict(help="""(string) api name """, choices=['describe-alarms','create-alarm','delete-alarms','describe-alarms-by-id','update-alarm','enable-alarm','disable-alarm','describe-alarm-history','describe-metrics','describe-metrics-for-create-alarm','describe-metric-data','put-metric-data',], required=True)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 生成单个API接口的json骨架空字符串 ''',
        description='''
            生成单个API接口的json骨架空字符串。

            示例: jdc nc generate-skeleton --api describeContainer ''',
    )
    def generate_skeleton(self):
        skeleton = Skeleton('monitor', self.app.pargs.api)
        skeleton.show()
