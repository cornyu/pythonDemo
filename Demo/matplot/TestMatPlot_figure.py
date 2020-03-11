# plt.figure()
# 你可以多次使用figure命令来产生多个图，其中，图片号按顺序增加。这里，要注意一个概念当前图和当前坐标。
# 所有绘图操作仅对当前图和当前坐标有效。通常，你并不需要考虑这些事，下面的这个例子为大家演示这一细节。

import matplotlib.pyplot as plt
plt.figure(1)                # 第一张图
plt.subplot(211)             # 第一张图中的第一张子图
plt.plot([1, 2, 3])
plt.subplot(212)             # 第一张图中的第二张子图
plt.plot([4, 5, 6])


plt.figure(2)                # 第二张图
plt.plot([4, 5, 6])            # 默认创建子图subplot(111)

plt.figure(1)                # 切换到figure 1 ; 子图subplot(212)仍旧是当前图
plt.subplot(211)             # 令子图subplot(211)成为figure1的当前图
plt.title('Easy as 1,2,3')   # 添加subplot 211 的标题

plt.show()
