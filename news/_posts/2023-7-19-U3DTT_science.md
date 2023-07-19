---
layout: post
title: ScienceAAAS报道｜一种深度学习辅助的水下三维触觉张拉整体传感器：大连海事大学徐敏义、北京大学谢广明和纳米能源所王中林院士合作进展
author: 
url_author: 
---

<p style="text-align:center;" >
<img class="center-block" style="margin:auto; width:70%;" src="/lab_images/news/U3DTT_research.png" alt=""/>
<b>
</b>
</p>


- 大连海事大学徐敏义教授团队，北京大学谢广明教授团队和中科院北京纳米能源所王中林院士团队展开合作提出一种深度学习辅助的水下三维触觉张拉整体（Underwater three dimension tactile tensegrity, U3DTT）传感器，该传感器可以实时测量和区分来自流场或与障碍物相互作用的扰动幅值、位置和方向，同时为水下航行器的运行提供碰撞保护。与水下二维触觉传感器相比，U3DTT展示出多自由度、超高灵敏度、快速响应时间、低成本和顺应性强等优点。这代表水下传感技术和应用方面的一个足够显著的进步。进一步，将U3DTT与AUV进行系统集成，在水池实验中U3DTT的实时三维位姿估计平均均方根误差为0.76，表明U3DTT能够将三维传感信息反馈给各种任务中的水下机器人，说明其在具有触觉反馈的机器人技术中的潜在应用价值。该成果以题为“Deep-Learning-Assisted Underwater 3D Tactile Tensegrity”发表Research上。

- Citaytion:

- Peng Xu, Jiaxi Zheng, Jianhua Liu, Xiangyu Liu, Xinyu Wang, Jiaxi Zheng, Siyuan Wang, Tianyu Chen, Hao Wang, Chuan Wang, Xianping Fu, Guangming Xie, Minyi Xu and Zhonglin Wang.
Deep-Learning-Assisted Underwater 3D Tactile Tensegrity. Research 2023;6:Article 0062. 
https://doi.org/10.34133/research.0062

> 研究背景

- 随着在海洋探索和研究中水下机器人应用的增长，迫切需要有效的三维触觉为水下机器人作业提供触觉反馈。张拉整体结构通常是由分离的刚性杆和张力元件构成，刚性杆通过连续的张力元件构成一个张力网络。这种轻型、多自由度和高动态顺应性的结构设计能够通过张力网络有效地重新分配载荷，允许系统被动地适应外界环境。这种能力可以使张拉整体通过其姿态估计来探索未知的水下环境，尤其是在狭窄的空间中光或声音存在反射问题时。此外，该轻型结构还可以提供高冲击弹性。摩擦纳米发电作为一种全新的机电转换方式，其最大优势在于能将环境中广泛分布的杂乱无章的机械扰动高效且自驱动地转换成电能或者电信号，因此在环境能量捕获和微扰动自驱动感知领域有广阔应用前景。因此，将摩擦纳米发电机与张拉整体结构相结合视为水下航行器在探索未知水下环境过程中可行的三维触觉感知方案。

> 研究进展

- U3DTT结构的感知部分主要由安装在刚性碳纤维杆端点的可挤压掌心型摩擦纳米发电机（cap-shaped pressing triboelectric nanogenerator，CP-TENG），和用于连接两根杆的可张拉胡须状摩擦纳米发电机（rope-shaped stretchable triboelectric nanogenerator，RS-TENG）组成（如图 1所示）。

<p style="text-align:center;" >
<img class="center-block" style="margin:auto; width:70%;" src="/lab_images/news/U3DTT_1.png" alt=""/>
<b>
图1  基于摩擦纳米发电机（TENG）的张拉整体结构图
</b>
</p>

- PP-TENG传感器可以在外加压力下将柔性盖变形转换为电信号。当传感器去除外加压力时，盖板在软材料的恢复力作用下恢复原状。RS-TENG的主体用乳胶管和铝合金夹子密封，在乳胶管和碳纳米管之间存在空气层，确保在水下环境中的拉伸力作用下RS-TENG能够产生摩擦电信号。图2和图3分别展示了PP-TENG和RS-TENG的力学性能。

<p style="text-align:center;" >
<img class="center-block" style="margin:auto; width:70%;" src="/lab_images/news/U3DTT_2.png" alt=""/>
<b>
图2  绳状可伸缩传感单元的工作机制和表征
</b>
</p>


<p style="text-align:center;" >
<img class="center-block" style="margin:auto; width:70%;" src="/lab_images/news/U3DTT_3.png" alt=""/>
<b>
图3  帽形传感单元的工作机制和表征
</b>
</p>

- 图4 展示了通过训练好的深度学习模型分析全周期输出信号，预测数据（蓝点）能够对实际数据（红线）进行很好的跟踪，对U3DTT的形变状态进行解算，进而评估水下航行器周围环境的信息。总体而言，这些能力展示基于U3DTT的水下触觉感知系统在自主探索未知水下环境中的巨大潜力。

<p style="text-align:center;" >
<img class="center-block" style="margin:auto; width:70%;" src="/lab_images/news/U3DTT_5.png" alt=""/>
<b>
图4  深度学习辅助的水下触觉感知系统
</b>
</p>

> 未来展望

- 本文设计了基于摩擦纳米发电和基于深度学习的数据分析的水下三维触觉张拉整体传感器，以探索未知环境，为水下航行器与其周围环境之间的相互作用提供一种技术方法，特别是当光学或声学反射问题发生在狭窄空间时。与其他二维触觉设备相比，DL辅助U3DTT提供多种先进的特性，包括多自由度、高灵敏度、低成本、快速响应时间和一致性。在未来的研究中，将着重于将基于摩擦纳米发电的水下仿生触觉感知作为水声以及视觉感知的重要补充。解决目前限制水下领域信息感知的各种问题，并通过水下智能设备为水下环境评估提供各种关键信息。


> 转载链接：

- 转载链接：https://mp.weixin.qq.com/s/d8NwSiFBIWIX7ieL4ujX-w

