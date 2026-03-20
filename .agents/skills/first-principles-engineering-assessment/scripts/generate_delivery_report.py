#!/usr/bin/env python3
"""Generate a markdown delivery report skeleton for engineering tasks."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a delivery report markdown skeleton."
    )
    parser.add_argument("task", help="Task title for this report")
    parser.add_argument(
        "-o",
        "--output",
        default="delivery_report.md",
        help="Output markdown file path (default: delivery_report.md)",
    )
    parser.add_argument(
        "--risk",
        default="P2",
        choices=["P0", "P1", "P2"],
        help="Initial risk level (default: P2)",
    )
    return parser.parse_args()


def build_report(task: str, risk: str) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""# 交付报告

1. 基本信息
1.1 任务：{task}
1.2 生成时间：{now}
1.3 风险等级：{risk}

2. 问题定义
2.1 目标：
2.2 非目标：
2.3 约束：

3. 事实与假设
3.1 事实：
3.2 假设（含验证方式）：

4. 方案与决策
4.1 方案 A（最小可行）：
4.2 方案 B（高扩展）：
4.3 选择与理由：

5. 改动清单
5.1 文件/函数：
5.2 行为变化：
5.3 不改动项：

6. 验证结果
6.1 测试/验证步骤：
6.2 结果：
6.3 未验证项：

7. 风险与处置
7.1 残余风险：
7.2 处置动作：
7.3 回滚条件：
"""


def main() -> int:
    args = parse_args()
    out_path = Path(args.output).expanduser().resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(build_report(args.task, args.risk), encoding="utf-8")
    print(f"Report generated: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
