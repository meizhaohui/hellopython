..  _18_upload_file_to_github_without_username_and_password:

github设置免密上传文件
==========================

.. contents:: 目录



生成密钥
~~~~~~~~

-  **ssh-keygen -t rsa -C “mzh.whut@gmail.com”**
   运行以上命令生成密钥，运行过程中一路按回车键(Enter)。命令执行完成后，会在家目录中生成.ssh目录，并生成两个文件：id_rsa(密钥)和id_rsa.pub(公钥)，使用NotePad++打开公钥id_rsa.pub，将其中的内容复制。

将公钥保存到github中
~~~~~~~~~~~~~~~~~~~~

-  登陆github后，依次打开\ **Settings**->**SSH and GPG
   keys**\ ，点击\ **New SSH
   key**\ ，将刚才复制的公钥id_rsa.pub内容粘贴到\ **Key**\ 输入框中，并指定一个\ **Title**\ 标题，并点击\ **Add
   SSH Key**\ 保存

本地git环境配置
~~~~~~~~~~~~~~~

设置用户名和邮箱
^^^^^^^^^^^^^^^^

-  设置用户名：\ **git config –global user.name “meizhaohui”**
-  设置邮箱：\ **git config –global user.email “mzh.whut@gmail.com”**
-  查看用户名设置是否生效：\ **git config user.name**
-  查看邮箱设置是否生效：\ **git config user.email**

设置git凭证存储
^^^^^^^^^^^^^^^

    如果你使用的是 SSH
    方式连接远端，并且设置了一个没有口令的密钥，这样就可以在不输入用户名和密码的情况下安全地传输数据。
    然而，这对 HTTP 协议来说是不可能的 ——
    每一个连接都是需要用户名和密码的。 “store”
    模式会将凭证用明文的形式存放在磁盘中，并且永不过期。
    这意味着除非你修改了你在 Git
    服务器上的密码，否则你永远不需要再次输入你的凭证信息。

-  新建存储凭证数据的文件，在git bash窗口，使用以下命令新建凭证存储文件
   **touch ~/.git-credentials**
-  将用户名和密码数据存储到凭证文件中，在~/.git-credentials文件中添加以下数据：*\*
   https://username:password@github.com \*\*
-  配置git凭证凭证存储：\ **git config –global credential.helper store**
-  注：git配置文件存放路径为：\ **~/.gitconfig**
-  ~/.git-credentials文件中,如果密码中包含特殊字符，需要进行urlEncode转义，如@符号需要写作%40，列举部分转换规则：

+------+-----------+--+
| 字符 | urlEncode |  |
+======+===========+==+
| #    | %23       |  |
+------+-----------+--+
| $    | %24       |  |
+------+-----------+--+
| +    | %2b       |  |
+------+-----------+--+
| @    | %40       |  |
+------+-----------+--+
| :    | %3a       |  |
+------+-----------+--+
| =    | %3d       |  |
+------+-----------+--+
| ?    | %3f       |  |
+------+-----------+--+

下载远程仓并测试修改上库
~~~~~~~~~~~~~~~~~~~~~~~~

-  使用以下命令进行远程仓的下载：\ **git clone
   https://github.com/meizhaohui/blog.git**
-  下载完成后，对下载的文件做一些修改，并保存
-  使用git diff查看修改差异：\ **git diff**
-  将修改文件添加到本地库：\ **git add -A**
-  添加commit信息：\ **git commit -m“commit log”**
-  查看远程仓信息： **git remote -v**
-  查看本地分支信息： **git branch**
-  将本地库中的修改push到远程仓库中： **git push origin master:master**
   (注：第一个master为本地分支，第二个master为远程分支)
