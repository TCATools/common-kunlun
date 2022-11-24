# -*- encoding: utf-8 -*-

# 2021-03-09    anakinliu   create

import csv
import logging
import os
import sys
import subprocess
import uuid

import json

logger = logging.getLogger(__name__)

class KunlunM(object):
    """
    """
    def run_cmd(self, cmd_args):
        """
        执行命令行
        """
        print("[run cmd] %s" % ' '.join(cmd_args))
        subprocess.Popen(cmd_args).wait()

    def format_issue(self, result_file):
        """
        """
        issues = []
        with open("map.json", 'rb') as rf:
            content = self._decode(rf.read())
            rule_map = json.load(content)
        if not os.path.exists(result_file):
            logger.warning("Result is empty")
        else:
            with open(result_file, 'r') as rf:
                reader = csv.reader(rf,delimiter=',')
                header = next(rf)  # 第一行为表头
                for line in reader:
                    path = line[5]
                    msg = line[3]
                    rule = rule_map[line[6]]
                    line_num = line[8]
                    column = 0
                    issues.append({
                        "rule": rule,
                        "path": path,
                        "msg": msg,
                        "line": line_num,
                        "column": column
                    })
            os.remove(result_file)
        with open('result.json', 'w') as wf:
            json.dump(issues, wf, indent=2)

    def run(self):
        """
        """
        source_dir = os.environ.get("SOURCE_DIR", "a")
        task_request_file = os.environ.get("TASK_REQUEST")
        with open(task_request_file, "r") as rf:
            task_request = json.load(rf)
        task_params = task_request["task_params"]
        rules = task_params['rules']
        with open("rule.json", "rb") as f:
            content = self._decode(f.read())
            rule_map = json.loads(content, strict=False)
        rules = ",".join([rule_map[x] for x in rules])
        del rule_map  # 清理变量
        result_file = os.path.join(os.getcwd(), "{}.csv".format(uuid.uuid1().hex))
        # result_file = "/Users/anakinliu/tools/Kunlun-M/a/result3.csv"
        cmd = ["python", "kunlun.py", "scan",
                "-t", source_dir, "-r", rules,
                "-o", result_file]
        logger.info(" ".join(cmd))
        self.run_cmd(cmd)
        self.format_issue(result_file)

    def _decode(self, text):
        # 如果本来就是字符串,直接返回
        if isinstance(text, str):
            return text
        try:
            # -*- 默认采用UTF-8解码
            return text.decode(encoding='UTF-8')
        except UnicodeDecodeError:
            # -*- 出现解码异常时，使用GBK解码且采取"surrogateescape"策略（表示只关注能正常解码的部分内容，其他内容使用unicode字符表示）
            # -*- 参考文档：https://docs.python.org/3/howto/unicode.html#files-in-an-unknown-encoding
            return text.decode(encoding="gbk", errors="surrogateescape")

if __name__ == "__main__":
    KunlunM().run()