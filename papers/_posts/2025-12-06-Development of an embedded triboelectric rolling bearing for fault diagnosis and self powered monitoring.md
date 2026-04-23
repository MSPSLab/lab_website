---
layout: paper
title: Development of an embedded triboelectric rolling bearing for faultdiagnosis and self-powered monitoring
image: "/lab_images/papers/0307-1.png"
authors: Fangyang Dong, Peishuo Li, Zhixiang Chen，Guang-An Yu，Hengxu Du , Zhiying Zhang , Weilu Sha , Yiyang Huo , Taili Du, Minyi Xu**
year: 2026
ref: Dong F, Li P, Chen Z, et al. Tribology International.
journal: "Tribology International 216 (2026) 111570"
pdf: "/pdfs/0307-1.pdf"
doi: 10.1016/j.triboint.2025.111570
type: journal
---

# Abstract

Smart bearings aim to integrate sensors and processing units into conventional bearing structures to enable condition monitoring and fault detection. In this study, a compact and practical embedded triboelectric bearing (TE-bearing) is designed and implemented for monitoring and detection in an actual rolling element bearing, enabled by triboelectrification occurring between its rolling elements and raceways. First, the effects of the embedded structure on bearing strength and electrical output are analyzed through finite element simulations and experiments, determining an optimal design that balances structural stability and signal-to-noise ratio. Then, an effective signal processing method is proposed via the characteristics of the acquired current signals to extract fault features. Experimental results show that the proposed transducer can successfully detect local faults in bearings through clear fault signatures in the current signals, which match the bearing characteristic frequency bands. Subsequently, the extracted features are validated using three classic machine learning algorithms, achieving an average accuracy above 98 % in fault classification. Compared to a reference accelerometer, the triboelectric transducer outperforms in frequency domain analysis. Moreover, the time-series dataset also performs well on four popular deep learning models, all of which exceed 96 % classification accuracy. Ablation studies using raw current signals reveal that the proposed time shifting method significantly enhances the performance of lightweight models. Finally, a self-powered demonstration of real-time bearing temperature monitoring is presented. All implementations utilize solely a commercial deep groove ball bearing and two copper sheets, demonstrating great potential for practical application and further improvement.
