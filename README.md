# skills workspace

个人自用的 Agent + Skill 规则仓库，用于复杂技术任务的决策、实施与交付留痕。

## 1. 文件结构
1.1 `AGENTS.md`：主规则（优先级、触发策略、输出策略、硬性约束）。  
1.2 `.agents/skills/first-principles-engineering-assessment/SKILL.md`：复杂任务执行细则。  
1.3 `.agents/skills/first-principles-engineering-assessment/references/checklists.md`：验证清单与交付模板。  
1.4 `.agents/skills/first-principles-engineering-assessment/scripts/generate_delivery_report.py`：报告骨架生成脚本。  

## 2. 调用策略（当前生效）
2.1 默认不调用 Skill，先走最小可行流程。  
2.2 命中关键词才调用 Skill：`评审`、`review`、`重构`、`最小可行实施计划`、`风险分级`、`验证证据`、`回滚方案`。  
2.3 非复杂任务（问答/查询/文案）不调用 Skill。  

## 3. 输出与交付基线
3.1 默认输出：结论 + 关键过程日志 + 必要证据。  
3.2 结构化输出使用三级编号：`1.` / `1.1` / `1.1.1`。  
3.3 交付必须包含：改动摘要、验证证据、残余风险。  

## 4. 快速使用
4.1 开始任务前先看 `AGENTS.md`，确认是否命中 Skill 关键词。  
4.2 需要留痕时用 `checklists.md` 记录验证结论。  
4.3 交付阶段生成报告骨架：

```bash
./.agents/skills/first-principles-engineering-assessment/scripts/generate_delivery_report.py "任务标题" -o delivery_report.md --risk P1
```

## 5. 最小自检
5.1 脚本可执行且能生成文件。  
5.2 文档编号连续且无跳号。  
5.3 评审类任务能输出问题清单（按严重级）与风险边界。  
