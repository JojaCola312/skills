# OpenClaw 原生 Windows 安装指南

声明：本文档仅适用于个人电脑环境下的 OpenClaw 部署与使用，不适用于生产环境、服务器环境或企业统一运维场景。使用者应自行评估账号、API key、本地文件、网络访问及消息渠道接入带来的安全风险。安装方式不唯一，也可参考部分国内大模型提供商（如智谱，火山引擎）和渠道提供商（如飞书，钉钉）的官方文档或官方平台说明。本文档仅提供操作说明，不对因部署、配置、密钥管理、大模型信息泄露或后续使用引发的安全后果承担责任。

## 1. 安装前准备
先安装以下软件：

- Node.js LTS：<https://nodejs.org/>
- Git for Windows：<https://git-scm.com/download/win>

安装完成后，打开 PowerShell 检查：

```powershell
node --version
npm.cmd --version
git --version
```

## 2. 打开 PowerShell
方法一：开始菜单搜索 `PowerShell` 并打开。  
方法二：按 `Win + R`，输入 `powershell.exe`，点击确定。

## 3. 安装 OpenClaw
在 PowerShell 中执行：

```powershell
npm.cmd install -g openclaw
```

安装完成后检查：

```powershell
openclaw.cmd --version
openclaw.cmd doctor
```

## 4. 准备 API key
### 大模型
建议优先选择以下国内平台之一，并先在平台官网创建 API key：

- 智谱 BigModel：<https://bigmodel.cn/>
- Kimi / Moonshot：<https://platform.moonshot.cn/>
- Qwen / 阿里百炼：<https://bailian.console.aliyun.com/>
- 火山引擎 Doubao：<https://www.volcengine.com/>

可以按需选择性价比更高的coding plan。

### 搜索
如需搜索能力，建议创建 Tavily API key：

- <https://tavily.com/>

## 5. 初始化 OpenClaw
在 PowerShell 中执行：

```powershell
openclaw.cmd onboard
```

如需参考初始化流程，可查看：

- <https://www.volcengine.com/docs/82379/2183190?lang=zh>

建议：
- 上述参考链接针对方舟引擎大模型，如果其他可以参考各自官方文档，区别主要是模型添加和通道添加
- 先准备好模型 API key 再执行 onboard
- workspace、gateway 保持默认值
- channels可以先跳过，如果有准备也可直接添加
- 如果准备了搜索引擎api，可以在此时添加

## 6. 打开 WebUI
执行：

```powershell
openclaw.cmd dashboard
```

如果浏览器没有自动打开：
- 复制终端输出的地址
- 手动粘贴到浏览器打开

## 7. 最小验证
执行：

```powershell
openclaw.cmd status
openclaw.cmd gateway restart
openclaw.cmd agent --agent main -m "Reply with exactly OK"
```

如果返回 `OK`，说明安装和模型接入正常。


## 8. 常用命令
以下为安装后最常用的基础命令：

```powershell
openclaw.cmd status
openclaw.cmd gateway restart
openclaw.cmd gateway stop
openclaw.cmd dashboard
openclaw.cmd onboard
openclaw.cmd doctor
```

说明：
- `openclaw.cmd status`：查看当前状态
- `openclaw.cmd gateway restart`：重启本地服务
- `openclaw.cmd gateway stop`：停止本地服务
- `openclaw.cmd dashboard`：打开 WebUI
- `openclaw.cmd onboard`：重新进入初始化配置
- `openclaw.cmd doctor`：检查环境与安装状态
## 9. 渠道配置参考
只保留官方文档入口，更详细的方式可以按需自行搜索：

- 飞书：<https://docs.openclaw.ai/channels/feishu>
<https://www.feishu.cn/content/article/7613711414611463386>
- 微信：<https://docs.openclaw.ai/zh-CN/channels/wechat>
- 钉钉：<https://open.dingtalk.com/document/dingstart/install-openclaw-locally>

## 10. 替代选项
国产有很多基于龙虾的产品，可按需自行选择，稳定性和安全性高于原生龙虾：

- 腾讯 workbuddy：<https://www.codebuddy.cn/work/>
- 腾讯 QClawu:<https://qclaw.qq.com/> 
- 阿里 钉钉悟空：<https://wukong.dingtalk.com/>
