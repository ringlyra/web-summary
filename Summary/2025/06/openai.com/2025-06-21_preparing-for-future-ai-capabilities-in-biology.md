---
title: 'Preparing for future AI capabilities in biology'
source: https://openai.com/index/preparing-for-future-ai-capabilities-in-biology/
author:
  - openai.com
published: ''
fetched: '2025-06-21T04:40:34.734798+00:00'
tags:
  - codex
  - openai
image: 
---

## 要約

OpenAIは、高度な**AI**が薬開発やワクチン設計を加速する一方、生物兵器作成にも使われ得るとして、そのリスクを抑える新たな取り組みを発表した。バイオ分野の専門家や政府機関と協力し、モデルを安全に運用するための評価データ整備、危険な指示を拒否する訓練、常時モニタリングと違反チェック、専門家によるレッドチーム、そして機密性を守る多層的な**セキュリティ**対策を展開。信頼できる研究機関には高度モデルを提供する方針も視野に入れつつ、未熟者による誤用や熟練者の悪用を防ぐため迅速な検証と連携を進めている。今後は政府や研究機関との協力を深め、バイオ防衛サミットの開催を通じて**AI**と**バイオ**の両面から安全体制を強化し、社会全体で長期的な備えを固める必要性を強調している。

## 本文

Advanced AI models have the power to rapidly accelerate scientific discovery, one of the many ways frontier AI models will benefit humanity. In biology, these models are [already helping scientists⁠(opens in a new window)](https://www.fiercebiotech.com/medtech/fine-tuned-ai-models-openai-babylon-aim-predict-clinical-trial-successes) identify which new drugs are most likely to succeed in human trials. Soon, they could also accelerate drug discovery, design better vaccines, create enzymes for sustainable fuels, and uncover new treatments for rare diseases to open up new possibilities across medicine, public health, and environmental science.

At the same time, these models raise important dual-use considerations: enabling scientific advancement while maintaining the barrier to harmful information. The same underlying capabilities driving progress, such as reasoning over biological data, predicting chemical reactions, or guiding lab experiments, could also potentially be misused to help people with minimal expertise to recreate biological threats or assist highly skilled actors in creating bioweapons. Physical access to labs and sensitive materials remains a barrier—however those barriers are not absolute.

We expect that upcoming AI models will reach ‘High’ levels of capability in biology, as measured by our [Preparedness Framework⁠(opens in a new window)](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf)*, and we’re taking a multi-pronged approach to put mitigations in place. In this post, we cover:

*   Developing a responsible approach to advancing biological capabilities
*   Collaborating with external domain experts including government entities and national labs
*   Training models to safely handle dual-use biological requests
*   Building detection, monitoring, and enforcement systems
*   Adversarial red-teaming our mitigations with experts
*   Deploying security controls
*   What’s ahead

Our approach
------------

We need to act responsibly amid this uncertainty. That’s why we’re leaning in on advancing AI integration for positive use cases like biomedical research and biodefense, while at the same time focusing on limiting access to harmful capabilities. Our approach is focused on prevention—we don’t think it’s acceptable to wait and see whether a bio threat event occurs before deciding on a sufficient level of safeguards.

The future will require deeper expert and government collaboration to strengthen the broader ecosystem and help surface issues that no single organization could catch alone. We’ve consulted with external experts at every stage of this work. Early on, we worked with leading experts on biosecurity, bioweapons, and bioterrorism, as well as academic researchers, to shape our biosecurity threat model, capability assessments, and model and usage policies. As we designed mitigations, human trainers with master’s and PhDs in biology helped create and validate our evaluation data. And now, we’re actively engaging with domain-expert red teamers to test how well our safeguards hold up in practice under high fidelity scenarios.

Even as we invest in further research, such as wet lab uplift studies to assess novices’ success on harmless proxy tasks, we are preparing and implementing mitigations now. We’re also continuing to partner closely with government entities, including the [US CAISI⁠(opens in a new window)](https://www.nist.gov/aisi) and [UK AISI⁠(opens in a new window)](https://www.aisi.gov.uk/). We’ve worked with [Los Alamos National Lab](https://openai.com/index/openai-and-los-alamos-national-laboratory-work-together/) to study AI’s role in wet lab settings and support external researchers advancing biosecurity tools and evaluations.

Our capability assessments, including those detailed in our system cards, are informed by expert input and designed to estimate when a model crosses into High thresholds. We recognize these assessments are based on hard-to-test assumptions about the bioweaponization pathways and can’t definitively predict real-world misuse. But given the stakes, we want to be proactive in taking relevant readiness measures.

Strengthening defenses in biology
---------------------------------

Over the past two years, we’ve tracked what our models can do as they develop, worked to reduce risks before launch per the [Preparedness Framework⁠(opens in a new window)](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf), and shared our findings openly through system cards so others can follow our progress. As part of this, we’ve built Preparedness evaluations that run during frontier model training to give early and regular snapshots of a model’s capabilities.

We’re sharing how we’re preparing, both what’s already in place and what’s ahead, while holding back sensitive details that could help bad actors get around our safeguards.

*   **Training the model to refuse or safely respond to harmful requests:** Historically, we’ve trained models to refuse dangerous requests. We will continue to do this for requests that are explicitly harmful or enable bioweaponization. For dual use requests (such as virology experiments, immunology, genetic engineering, etc.), we follow the principles outlined in our [Model Spec⁠(opens in a new window)](https://model-spec.openai.com/2025-04-11.html), including avoiding responses that provide actionable steps. We believe that detailed step-by-step instructions and wet lab troubleshooting guidance can be risky in the wrong hands. Our default behavior for the general public will intentionally err on the side of caution, by training models to provide high-level insights that support expert understanding while withholding sufficient detail to prevent novice misuse.
*   **Always-on detection systems:** We’ve deployed robust system-wide monitors across all product surfaces with frontier models to detect risky or suspicious bio-related activity. If it looks unsafe based on our filters, the model response is blocked. This also triggers automated review systems, and human review is initiated when needed.
*   **Monitoring and enforcement checks:** We prohibit use of our products to cause harm, and we enforce our policies when we see misuse. We use the same advanced AI reasoning capabilities to detect biological misuse, combining our automated systems with human reviewers to monitor and enforce our policies. Misuse can result in suspension of accounts. We take misuse related to biological risk seriously and may conduct additional investigation into the user and, in egregious cases, we may notify relevant law enforcement. You can read more about our moderation practices [here](https://openai.com/transparency-and-content-moderation/).
*   **End-to-end red teaming:** We are working with multiple teams of expert red teamers; people who try to break our safety mitigations. Their job is to try to bypass all of our defenses by working end-to-end, just like a determined and well-resourced adversary might. This helps us identify gaps early and strengthen the full system. Red-teaming in the biology domain comes with its own challenges. Most expert red teamers lack biorisk domain expertise and may not be able to judge the harmfulness of model output. Most domain experts in biology are not experienced in exploiting model vulnerabilities. We are engaging with both groups to test different aspects of our system from risk coverage to robustness, and pairing them up in teams for the most sophisticated red teaming.
*   **Security controls:** We take a defense-in-depth approach to protecting our model weights, relying on a combination of access control, infrastructure hardening, egress controls, and monitoring. We leverage purpose-built detections and controls to mitigate the risk of exfiltration of high-risk model weights. We complement these measures with always-on Detection & Response, dedicated Threat Intelligence, and an Insider-Risk program ensuring emerging threats are identified and blocked quickly.

Our Board’s [Safety and Security Committee](https://openai.com/index/update-on-safety-and-security-practices/) has reviewed our approach, and we’ve already rolled out initial versions of this end-to-end mitigation plan in many current models, like o3, which remain below the High capability threshold in our Preparedness Framework. Through this process, we have used the learnings we gained through our deployments to significantly improve the performance of our technical systems and work out the kinks in our human review workflows. We will continue to make changes as we learn more.

What’s ahead
------------

While we’re focused on securing our own models, we recognize that not all organizations will take the same precautions, and the world may soon face the broader challenge of widely accessible AI bio capabilities coupled with increasingly available life-sciences synthesis tools.

We’re hosting a biodefense summit this July, bringing together a select group of government researchers and NGOs to explore dual-use risks, share progress, and explore how our frontier models can accelerate research. Our goal is to deepen our partnerships with the U.S. and aligned governments, and to better understand how advanced AI can support cutting edge biodefense work, from countermeasures to novel therapies, and strengthen collaboration across the ecosystem.

While our safety work aims to limit broad misuse, we’re also developing policy and content-level protocols to grant vetted-institutions access to maximally helpful models so they can advance biological sciences. That includes partnerships to develop diagnostics, countermeasures, and novel testing methods.

Building off of our safety work with governments, we believe the public and private sectors should work together to strengthen our society’s biological defenses outside of AI models. This could include strengthened nucleic acid synthesis screening (building on [the recent Executive Order⁠(opens in a new window)](https://www.whitehouse.gov/presidential-actions/2025/05/improving-the-safety-and-security-of-biological-research/)), more robust early detection systems for novel pathogens, hardening infrastructure against biothreats, and investing in biosecurity innovations to help ensure long-term resilience against biological threats.

We also believe that complementary advances in AI and biosecurity research will increasingly provide fertile ground for founders to build new mission-driven startups that can harness the entrepreneurial spirit to help solve these challenges. Safety and security are not just aspects of AI models and products—they are increasingly indispensable services and sectors that will pencil out for investors. We will be actively involved in accelerating this.

We look forward to more collaboration with governments, researchers, and entrepreneurs around the world—not only to ensure that the biosecurity ecosystem is prepared, but to take advantage of the astonishing breakthroughs that are still to come.
