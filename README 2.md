# 论文库模板

以 GitHub 仓库保存论文概括和 PDF，在多台电脑上用 VS Code 编辑。网站使用 MkDocs Material，主页只展示论文名与标签，支持搜索与标签筛选，没有阅读进度或状态。

## 1. 本地打开

安装 Python 3.11+、Git 和 VS Code。解压后，在 VS Code 中打开包含 `mkdocs.yml` 的文件夹，在终端运行：

macOS / Linux：

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m mkdocs serve
```

Windows PowerShell（无需激活环境）：

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m mkdocs serve
```

打开 http://127.0.0.1:8000/ ，修改 Markdown 后预览自动更新。Ctrl+C 停止。

## 2. 新增论文

1. 复制 `templates/paper.md` 到 `docs/papers/your-paper.md`。
2. 填写顶部元数据和正文标题、作者、概括。
3. 自由填写标签，例如 `LEO`、`ML`、`Scheduling`；标签菜单自动生成，无需修改代码。大小写应统一。
4. 把 PDF 放到 `docs/pdfs/your-paper.pdf`，在笔记中加入 `[打开 PDF](../pdfs/your-paper.pdf)`；也可以填入原文的 HTTPS 链接。
5. 删除“原文尚未添加”和不用的模板提示。

主页和导航自动收录 `docs/papers/` 下的所有 Markdown，无需手动维护目录。文件名建议用英文小写和连字符。删除四个示例文件即可开始自己的论文库；示例不包含真实 PDF 或经核实的论文概括。

默认使用 PDF 链接，由浏览器打开原文。需要在概括页内嵌时，可以自行加入下面这段 HTML，路径需与实际文件一致：

```html
<object data="../pdfs/your-paper.pdf" type="application/pdf" width="100%" height="900">
  <a href="../pdfs/your-paper.pdf">打开 PDF</a>
</object>
```

在 GitHub 上直接看 Markdown 时，使用普通 PDF 链接；内嵌预览用于生成的网站。

## 3. 创建 GitHub 仓库

在 GitHub 创建一个空仓库，例如 `paper-library`。初始创建时不要勾选自动生成 README、许可证或 .gitignore，避免与本地文件冲突。在本项目目录执行（替换 YOUR-USERNAME）：

```sh
git init
git add .
git commit -m "Create paper library"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/paper-library.git
git push -u origin main
```

也可使用 GitHub Desktop 完成初始化、发布和同步。项目中不存放登录令牌。`.gitignore` 已排除虚拟环境与生成的网站。若要将仓库重复用作其他论文库起点，可在仓库设置中启用 Template repository。

## 4. 在另一台电脑工作

```sh
git clone https://github.com/YOUR-USERNAME/paper-library.git
cd paper-library
```

然后按第 1 节在该电脑单独创建环境。每次开始修改前：

```sh
git pull --ff-only
```

完成后：

```sh
git status
git add docs
git commit -m "Add or update paper notes"
git push
```

如果还修改了配置或 README，另外把对应文件加入提交。换电脑前先提交并推送，到另一台电脑后先拉取。这不是实时同步；不要依赖关闭 VS Code 自动上传。PDF 是二进制文件，同一份 PDF 避免同时改动。

若推送提示远端有新提交，先保留本地修改，再拉取并合并；如有冲突，在 VS Code 中核对两边内容后提交，不要用强制推送覆盖其他电脑的记录。多人协作建议各自建分支，通过 Pull Request 合并。

## 5. 网站发布（可选）

仓库本身已经可以查看 Markdown 和同步资料；不发布网站也能使用。

需要 GitHub Pages 时：在仓库 Settings → Pages 中选择 GitHub Actions，然后在 Actions 中手动运行 **Publish library**。每次想更新网站时再次运行。发布流程不会因普通推送自动启动；日常推送只执行构建检查。

可在 `mkdocs.yml` 中设置 `site_url: https://YOUR-USERNAME.github.io/paper-library/`。Pages 地址以部署结果为准。本站点未替你上传或发布。发布的静态文件包含 `docs/pdfs/` 中的 PDF，发布前请确认这些文件适合向网站受众提供。

## 6. 验证和目录

```sh
python -m mkdocs build --strict
```

生成结果位于 `site/`。交付包中包含构建好的副本；可用 `python -m http.server 8000 --directory site` 预览。全文搜索请通过 HTTP 访问，避免直接双击 HTML。

```text
docs/index.md         主页介绍
docs/papers/          每篇论文的概括与元数据
docs/pdfs/            原文 PDF
docs/assets/          列表搜索与样式
templates/paper.md    新论文模板
hooks/library.py     根据 Markdown 自动生成列表
.github/workflows/   构建检查与手动发布
```

主页搜索覆盖标题、作者、标签；顶部主题搜索覆盖笔记正文。无 JavaScript 时仍显示完整论文列表。
