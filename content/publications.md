<!--
  PUBLICATIONS: shown in the "Publications" section of the home page.

  Structure:
    ## Group heading          (e.g. Journal & Conference, Thesis, Reports & Posters)
    ### Paper title
    - authors: ...            (wrap your own name in **bold**)
    - venue: ...              (*italics* for journal/conference names; end with the year)
    - date: YYYY-MM-DD        (optional; exact publication date for search engines)
    - links: [Paper](url) [Code](url) [Blog](/blogs-posts/posts/...)
    Abstract paragraph(s)     (optional; shown by the "Abstract" button)

  Entries appear in the order written here. A doi.org link in "links" also lists the
  paper in the page's structured data for Google Scholar / search engines.
  Save: `npm run dev` refreshes the page; `npm run build` / pushing to master publishes it.
-->

## Journal & Conference

### Tactical vs. strategic: An adaptable framework for horizon-dependent dengue forecasting using data-driven approaches with serotype and climate covariates in Bangladesh
- authors: **Md. Muqtadir Fuad**, Md. Sajib Milki, [Ridwan Al Aziz](https://ipe.buet.ac.bd/faculty/ridwan-al-aziz)
- venue: *PLOS ONE*, 2026
- date: 2026-08-21
- links: [Paper](https://doi.org/10.1371/journal.pone.0353069) [Data](https://doi.org/10.5281/zenodo.19589534) [Blog](/blogs-posts/posts/blog-dengue.html)

Dengue remains a major public health problem in endemic regions, including Bangladesh. Forecasting algorithms relying on climatic variables may not capture epidemiological information such as dengue serotype patterns. This study proposes a horizon-dependent dengue forecasting framework and applies it to Bangladesh. This pipeline included temporal, meteorological, demographic, and epidemiological covariates in a district-panel pipeline and compares classical, machine-learning, and deep-learning algorithms using aggregate, horizon-wise, regime-wise, outbreak-detection, and uncertainty metrics. Coefficient-based interpretation, SHAP, permutation importance, and nonlinear causal-dependence analysis were used to examine predictor impacts across horizons. SARIMAX was used as the baseline model. TFT produced quantile forecasts but showed poor interval calibration during outbreak periods. Results show that no single model performed best across all forecasting horizons: SARIMAX ranked highest for one-step outbreak alerting (precision = 0.886, recall = 0.824, F1 score = 0.854, and ROC-AUC = 0.950), whereas Prophet performed best for pooled magnitude forecasting at horizons 2–6. MLR showed competitive performance in regime-wise evaluation. These findings show that dengue forecasting algorithms should be selected according to the intended decision objective and evaluated using task-relevant protocols.

### eGov-Lens: A Multi-Dimensional Machine Learning Approach to Aspect-Based Public Feedback Analysis on Bengali e-Government Platforms
- authors: **Md. Muqtadir Fuad**, Abdullah Al Mazid, Md. Istiak Adnan, Tirthojit Das, Shatabdi Sen Prapti, Nafisa Mahbub
- venue: *28th International Conference on Computer and Information Technology (ICCIT)*, 2025
- links: [Paper](https://doi.org/10.1109/ICCIT68739.2025.11491291) [Code & Data](https://github.com/md-muqtadir-fuad/eGov-Lens) [Blog](/blogs-posts/posts/blog-egov-lens.html)

With the rapid expansion of e-services under Digital Bangladesh initiatives, citizens increasingly rely on online platforms to access government services and most often share their opinion in social media and digital forums. Existing sentiment analysis lacks of aspect-level insights in terms of egovernment related services. This paper presents eGov-Lens, a practical pipeline for aspect-based analysis of Bengali public feedback on e-government channels. We curate and annotate 34,001 comments (2020-2024) spanning twelve services and four policy-relevant aspects- sentiment, ease of find, responsiveness, and accuracy. The approach benchmarks three text representations (bag-of-words/CountVectorizer, BanglaBERT, mBERT) with logistic regression, support vector classifier, and naïve bayes. BanglaBERT with a support-vector head attains the strongest single-aspect quality on the policy-critical Accuracy task (micro-avg accuracy ≈0.93), while BanglaBERT with logistic regression offers the best accuracy-latency trade-off for deployment and a classical CountVectorizer+LR baseline trains and infers fastest. An entropy-weighted TOPSIS combines quality and cost to rank alternatives, favoring CountVectorizer+LR overall with BanglaBERT+LR a close second, and providing actionable guidance for NLP deployment on resource-constrained government infrastructure.

### Stochastic Modeling of Throughput-Quality Dynamics in Labor-Intensive Manufacturing: A Comparative Analysis of Operator Fatigue and Process Instability
- authors: **Md. Muqtadir Fuad**, Abdullah Al Mazid, Md. Istiak Adnan, Khalid Ammar
- venue: *8th IEOM Bangladesh International Conference on Industrial Engineering and Operations Management*, 2025
- links: [Paper](https://doi.org/10.46254/BA08.20250379)

The inherent variability of manual assembly processes presents significant challenges to standardization and quality assurance within the semi-automated food production sector. This study presents a quantitative and comparative analysis of the stochastic nature of human fatigue and its effect on productivity. By integrating high-resolution time-motion analysis with statistical process control (SPC), the research investigates two manual production lines to quantify quality parameters and examine relationships among product shape, operator performance behavior, efficiency, and unit weight consistency. Regression analysis was employed to estimate the relationship between time and worker fatigue in a controlled environment. Furthermore, process capability analysis reveals the relationship between human fatigue and process instability. Finally, using a Monte Carlo algorithm, the study simulates data to quantify annual financial loss due to process instability.

### Aerodynamic Performance Analysis of NACA 4415 Airfoil Incorporating Gurney and Bionic Flap: A Steady-State Numerical Analysis
- authors: Md Zisanul Haque Bhuiyan, **Md. Muqtadir Fuad**, Masud Rana, A. S. M. Maruf Hasan, Khalid Ammar
- venue: *7th Bangladesh Conference on Industrial Engineering and Operations Management*, 2024
- links: [Paper](https://doi.org/10.46254/BA07.20240040)

NACA 4415 is one of the most common and widely studied airfoils in aerodynamic research. Incorporating flaps with the NACA 4415 airfoil is an effective way to improve aerodynamic performance and efficiency. This study presents a comparative numerical analysis among a standard NACA 4415 airfoil, a modified NACA 4415 airfoil incorporating a Gurney flap, and a NACA 4415 airfoil incorporating a bionic flap based on the coefficient of lift and coefficient of drag at various angles of attack, including -15°, -10°, -5°, 0°, 5°, 10°, and 15°, with a flap height of 2% of the chord length. The airfoil performance was evaluated under a constant upstream velocity of 20 m/s using Computational Fluid Dynamics simulations. Performance was measured based on the lift-to-drag coefficient ratio and validated using velocity and pressure contours over the surface of the airfoil. The highest lift-to-drag ratio was found in the NACA 4415 airfoil incorporating a Gurney flap, followed by the standard NACA 4415 airfoil, while the NACA 4415 airfoil incorporating a bionic flap showed the lowest ratio. At 0° angle of attack, the Gurney flap improved the lift-to-drag ratio by 49.9% compared to the standard airfoil, while the bionic flap reduced the ratio by 19.86%. Overall, the NACA 4415 airfoil with Gurney flap outperformed the other two airfoil configurations, and the velocity and pressure contours supported the results obtained from lift and drag coefficients.

## Preprints & Under Review

### A Physics-Informed Hybrid Forward-Inverse Machine Learning Framework for High-Dimensional Sparse Recipe Reconstruction
- authors: **Md. Muqtadir Fuad**, Md. Istiak Adnan, [Ridwan Al Aziz](https://ipe.buet.ac.bd/faculty/ridwan-al-aziz)
- venue: Under review, 2026
- links: [arXiv](https://arxiv.org/abs/2610.14097)

High-dimensional sparse recipe formulation in process industries involves nonlinear association of various covariates, bounded by sparsity constraints and multi-criteria tolerances. Traditional physics-based classical methods (such as Kubelka-Munk) fail to generate sparse candidate recipes properly due to their simplified assumptions and industrial process variations. This study proposes a hybrid physics-informed uncertainty-aware framework that is structured into three modules: (a) Module A, a multi-target forward quality model; (b) Module B, a sparse inverse reconstructor; and (c) Module C, a feasibility-constrained ranking layer. Then it has been validated in an industrial textile dyeing context with recipe-grouped cross-validation under multi-illuminant quality assessment comprising process and production information, target reflectance, K/S values, and spectral descriptors. Histogram Gradient Boosting (HGB) with spectral-only features (Rλ, K/S) and Gradient Boosting Regressor (GBDT) with recipe-process features outperforms other configurations with out-of-Fold MAE of 0.1655 and 0.1523 in the forward quality model. For inverse reconstruction, a component-wise median blend achieved a recipe-vector MAE of 0.0295. Exploratory conditional treatment effect (CATE) suggests an observational association that alkali adjustment reduces error for red and pale shades (CATE = -0.196). This framework provides a human-in-the-loop decision-support tool that minimizes costly laboratory trials across industrial formulation domains.

## Thesis

### Data-Driven Color Recipe Recommendation System for Reactive Dyeing of Cotton and Blended Knit Fabrics
- authors: **Md. Muqtadir Fuad**, Md. Istiak Adnan · Supervisor: [Dr. Ridwan Al Aziz](https://ipe.buet.ac.bd/faculty/ridwan-al-aziz)
- venue: Undergraduate Thesis, Dept. of IPE, BUET, 2026
- links: [Blog](/blogs-posts/posts/blog-ug-thesis.html)

Reactive dye recipe development for cotton and blended knit fabrics depends on historical shade-matching, laboratory trials, and CMC-based color evaluation in industry. This thesis presents a data-driven recipe recommendation framework built from industrial shade-matching records. The dataset includes target shade information, fabric and fiber composition, dye formulations, and instrumental color measurements. The framework used historical similarity retrieval, dye-name prediction using supervised learning, dye-percentage regression and ΔE-based quality prediction. The historical baseline performed better for candidate retrieval. It achieved 0.7821 component dye accuracy, 0.6154 exact sequence accuracy, and 0.7692 top-3 dye-set accuracy. For top-1 prediction, the Gradient Boosting recipe outperforms baseline, with 0.8269 component accuracy, 0.6538 exact sequence accuracy, and 0.6538 top-1 dye-set accuracy. Its dye-percentage model achieved 0.2750 total recipe percentage MAE. The Extra Trees quality model predicted maximum ΔE with 0.1492 MAE, and 72.44% of predictions were within ±0.20 ΔE. The results show that a hybrid framework beats single model: historical retrieval improves candidate coverage, supervised learning improves top-1 recipe prediction, and ΔE estimation supports risk-based ranking.

## Reports & Posters

### Semi-Automated Shoe Cleaning Machine: Design, Simulation, and Feasibility Analysis
- authors: **Md. Muqtadir Fuad**, Abdullah Al Mazid, Md. Ashiqur Rahman Noor, Md Sadiqul Haque, Ananya Halder, Yashna Noor
- venue: Capstone Engineering Design Report, Dept. of IPE, BUET, 2024
- links: [Report](/blogs-posts/posts/blog-semi-automated-shoe-cleaning-machine.html)

The “Semi-Automated Shoe Cleaning Machine” report presents a comprehensive study conducted in the context of Bangladesh, focusing on the development and evaluation of an innovative cleaning solution that combines traditional cleaning methods with semi-automated technology. In a country where efficient and hygienic cleaning solutions are becoming increasingly necessary, this product is designed to cater to individuals and small businesses seeking an affordable and user-friendly shoe cleaning solution. Based on the market survey results, we determined the customer requirements and technical specifications, along with their relationships and correlations. We then conducted qualitative analysis of material, manufacturing processes, and joining process selections. Following this, we performed quantitative analyses by calculating relative emphasis coefficients using the Digital Logic Method and performance indices. Additionally, we conducted equivalent (von Mises) stress, total deformation, fatigue life, and fatigue safety factor analyses using Ansys. Finally, we performed cost, breakeven, and sensitivity analyses for our product.

### IoT-Based Smart Conveyor System for Integrated Quality, Inventory and Process Control
- authors: **Md. Muqtadir Fuad**, Abdullah Al Mazid, Md. Ahabab Ul Haq, Most. Noshin Ibnat, Chowdhury Mouinur Rahman, Nafis Ahmad
- venue: Technical Poster, 2024
- links: [Poster](https://doi.org/10.13140/RG.2.2.25476.23683) [Video](https://youtu.be/_iA_Y-_De4U) [Blog](/blogs-posts/posts/blog-iot-conveyor.html)

This project presents an IoT-based smart conveyor system designed for automated weight-triggered operation and real-time inventory tracking. Using a 5kg load cell with an HX711 amplifier, the system detects when an item's weight exceeds a preset threshold (e.g., 200 grams) to start the conveyor motor controlled by an L298N driver and a 6V 600RPM DC gear motor. A mechanical arm, operated by an SG-90 micro servo motor, places items onto the conveyor belt. The HC-SR04 ultrasonic sensor detects and counts each passing item, providing immediate visual feedback through a green LED. The ESP32 microcontroller enables IoT connectivity, allowing remote monitoring and real-time data logging of weight, item count, and system status for efficient inventory management and process control. This automated setup enhances accuracy, efficiency, and quality assurance in manufacturing lines.
