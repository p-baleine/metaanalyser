# A Systematic Review of Programming Testing Arxiv

This systematic review explores the field of programming testing arxiv, which aims to solve the problem of software errors. It covers the historical background of the field and its future development. The review includes five papers that discuss new approaches for generating test cases, benchmark datasets for machine learning research, novel techniques for program synthesis, feasibility and effectiveness of test case generation for program repair, and combinatorial testing for deep learning systems.

## Table of contents

1. Introduction: This section provides an overview of the field of programming testing arxiv and its importance in solving the problem of software errors.
2. Metamorphic Testing for Generating Next Test Cases: This section discusses the concept of metamorphic testing and its potential to reveal software errors that are left undetected in successful test cases. It also explores the limitations of current software testing techniques and proposes a novel test case selection technique.
    1. Background: This subsection provides a brief history of software testing and its importance in software development.
    2. Metamorphic Testing: This subsection explains the concept of metamorphic testing and how it can be used to generate new test cases from successful ones.
    3. Limitations of Current Software Testing Techniques: This subsection explores the limitations of current software testing techniques and how metamorphic testing can augment their effectiveness.
    4. Proposed Test Case Selection Technique: This subsection discusses the proposed test case selection technique and how it can help uncover software errors in the production phase.
3. Codexglue for Machine Learning Research: This section introduces CodeXGLUE, a benchmark dataset for machine learning research in program understanding and generation. It also discusses the impact of benchmark datasets on accelerating research in programming language tasks.
    1. Background: This subsection provides a brief history of benchmark datasets and their importance in machine learning research.
    2. CodeXGLUE: This subsection introduces CodeXGLUE, a benchmark dataset for machine learning research in program understanding and generation.
    3. Impact of Benchmark Datasets on Accelerating Research: This subsection discusses the impact of benchmark datasets on accelerating research in programming language tasks.
4. Neuro-Symbolic Program Synthesis: This section proposes a novel technique, Neuro-Symbolic Program Synthesis, to overcome the limitations of neural architectures for program induction. It also explains how the proposed technique can automatically construct computer programs in a domain-specific language that are consistent with a set of input-output examples provided at test time.
    1. Background: This subsection provides a brief history of neural architectures for program induction and their limitations.
    2. Neuro-Symbolic Program Synthesis: This subsection explains the concept of Neuro-Symbolic Program Synthesis and how it can overcome the limitations of neural architectures for program induction.
    3. Automatically Constructing Computer Programs: This subsection explains how the proposed technique can automatically construct computer programs in a domain-specific language that are consistent with a set of input-output examples provided at test time.
5. Test Case Generation for Program Repair: This section investigates the feasibility and effectiveness of test case generation in alleviating the overfitting issue in test suite based program repair techniques. It also proposes two approaches for using test case generation to improve test suite based repair.
    1. Background: This subsection provides a brief history of program repair techniques and their limitations.
    2. Feasibility and Effectiveness of Test Case Generation: This subsection investigates the feasibility and effectiveness of test case generation in alleviating the overfitting issue in test suite based program repair techniques.
    3. Proposed Approaches for Using Test Case Generation: This subsection proposes two approaches for using test case generation to improve test suite based repair.
6. Combinatorial Testing for Deep Learning Systems: This section explores the challenges of testing deep learning systems and proposes combinatorial testing as a promising avenue for testing such systems. It also adapts the concept of combinatorial testing and proposes a set of coverage criteria for deep learning systems.
    1. Background: This subsection provides a brief history of deep learning systems and their challenges in testing.
    2. Combinatorial Testing: This subsection explains the concept of combinatorial testing and how it can be used to reduce the testing space while obtaining relatively high defect detection abilities.
    3. Coverage Criteria for Deep Learning Systems: This subsection proposes a set of coverage criteria for deep learning systems.
7. Conclusion: This section summarizes the main findings of the systematic review and discusses future research directions in programming testing arxiv.

## Introduction

Software errors can cause significant damage to the production system and lead to financial losses. Therefore, software testing is an essential part of software development to ensure the quality of the software. However, the limitations of current software testing techniques have been observed [^1]. Firstly, successful test cases that do not reveal software errors are usually not further investigated, although they may contain useful information for revealing software errors. Secondly, errors may still exist in the software even after extensive testing in the development phase, and techniques for uncovering software errors in the production phase are seldom addressed in the literature. Thirdly, the availability of test oracles is pragmatically unattainable in most situations, but it is generally assumed in conventional software testing techniques. 

To address these limitations, the field of programming testing arxiv has emerged, which aims to develop new techniques for generating test cases, benchmark datasets for machine learning research, novel techniques for program synthesis, and testing deep learning systems [^1][^2][^3][^4][^5]. This systematic review explores the field of programming testing arxiv and its importance in solving the problem of software errors. It covers the historical background of the field and its future development. The review includes five papers that discuss new approaches for generating test cases, benchmark datasets for machine learning research, novel techniques for program synthesis, feasibility and effectiveness of test case generation for program repair, and combinatorial testing for deep learning systems.

## Metamorphic Testing for Generating Next Test Cases

Metamorphic testing is a new approach for generating next test cases that aims to reveal software errors that are left undetected in successful test cases [^1]. The current artifacts of software testing have limitations, including the assumption that successful test cases that do not reveal software errors are not further investigated. However, these successful test cases may still contain useful information for revealing software errors [^1]. Additionally, errors may still exist in the software even after extensive testing has been conducted in the development phase, and techniques for uncovering software errors in the production phase are seldom addressed in the literature [^1]. 

Metamorphic testing proposes a novel test case selection technique that derives new test cases from the successful ones, augmenting the effectiveness of existing test selection strategies [^1]. The selection aims to reveal software errors that are possibly left undetected in successful test cases generated using some existing strategies [^1]. The proposed technique can also help uncover software errors in the production phase and can be used in the absence of test oracles [^1]. 

The limitations of current software testing techniques can be overcome by using metamorphic testing, which generates new test cases from successful ones and helps uncover software errors that are left undetected [^1].

### Background: This subsection provides a brief history of software testing and its importance in software development.

Software testing is an essential part of software development that aims to identify and correct errors in software systems. As stated by [^1], software testing involves constructing a set of test cases according to some predefined selection criteria and examining the software against these test cases. The importance of software testing lies in its ability to ensure the quality and reliability of software systems. However, despite the extensive testing conducted during the development phase, errors may still exist in the software [^1]. These errors, if left undetected, may eventually cause damage to the production system. Therefore, the study of techniques for uncovering software errors in the production phase is crucial. Additionally, the availability of test oracles is pragmatically unattainable in most situations [^1]. However, the availability of test oracles is generally assumed in conventional software testing techniques. Therefore, new approaches for generating test cases and augmenting the effectiveness of existing test selection strategies are needed to improve the quality and reliability of software systems.

### Metamorphic Testing

Metamorphic testing is a new approach for generating next test cases from successful ones [^1]. The technique aims to reveal software errors that are possibly left undetected in successful test cases generated using some existing strategies. The proposed technique augments the effectiveness of existing test selection strategies and helps uncover software errors in the production phase. The selection of new test cases is based on the output of the successful test cases, and the technique can be used in the absence of test oracles [^1]. Metamorphic testing can be used with other test case selection strategies and can be combined with program checkers to suggest further testing [^1]. The approach requires problem domain knowledge, and a domain-specific methodology should be developed to facilitate the development of such a methodology [^1].

### Limitations of Current Software Testing Techniques

Current software testing techniques have limitations that can result in undetected errors in software systems [^1][^5]. Successful test cases that do not reveal software errors are usually not further investigated, even though they may contain useful information for revealing software errors [^1]. Additionally, errors may still exist in the software even after extensive testing has been conducted in the development phase, and techniques for uncovering software errors in the production phase are seldom addressed in the literature [^1]. Furthermore, the availability of test oracles is pragmatically unattainable in most situations, but it is generally assumed in conventional software testing techniques [^1]. However, metamorphic testing can augment the effectiveness of existing test selection strategies by deriving new test cases from successful ones, which aims at revealing software errors that are possibly left undetected in successful test cases [^1]. The proposed technique can also help uncover software errors in the production phase and can be used in the absence of test oracles [^1].

### Proposed Test Case Selection Technique

In software testing, a set of test cases is constructed according to some predefined selection criteria. The software is then examined against these test cases. However, an error-revealing test case is considered useful while a successful test case which does not reveal software errors is usually not further investigated. Whether these successful test cases still contain useful information for revealing software errors has not been properly studied [^1]. To address this issue, a novel test case selection technique is proposed that derives new test cases from the successful ones. The selection aims at revealing software errors that are possibly left undetected in successful test cases which may be generated using some existing strategies. As such, the proposed technique augments the effectiveness of existing test selection strategies. The technique also helps uncover software errors in the production phase and can be used in the absence of test oracles [^1].

## Codexglue for Machine Learning Research

This section introduces CodeXGLUE, a benchmark dataset for machine learning research in program understanding and generation. CodeXGLUE includes a collection of 10 tasks across 14 datasets and a platform for model evaluation and comparison [^2]. The availability of such data and baselines can help the development and validation of new methods that can be applied to various program understanding and generation problems. Benchmark datasets have a significant impact on accelerating research in programming language tasks [^2].

### Background: A Brief History of Benchmark Datasets and Their Importance in Machine Learning Research

Benchmark datasets have played a significant role in accelerating research in programming language tasks and machine learning. As stated by [^2], benchmark datasets provide a platform for the development and validation of new methods that can be applied to various program understanding and generation problems. They also enable researchers to compare the performance of different models and algorithms on a standardized set of tasks. Benchmark datasets have been used in various fields, including computer vision, natural language processing, and speech recognition, to name a few. The availability of such data and baselines can help researchers to develop new methods and improve the state-of-the-art in the field.

### CodeXGLUE: A Machine Learning Benchmark Dataset for Code Understanding and Generation

CodeXGLUE is a benchmark dataset for machine learning research in program understanding and generation [^2]. It includes a collection of 10 tasks across 14 datasets and a platform for model evaluation and comparison. CodeXGLUE also features three baseline systems, including the BERT-style, GPT-style, and Encoder-Decoder models, to make it easy for researchers to use the platform. The availability of such data and baselines can help the development and validation of new methods that can be applied to various program understanding and generation problems. Benchmark datasets have a significant impact on accelerating research in programming language tasks, and CodeXGLUE is the first diversified benchmark dataset that can be applied to various code intelligence problems [^2].

### Impact of Benchmark Datasets on Accelerating Research

Benchmark datasets have been shown to have a significant impact on accelerating research in programming language tasks [^2]. The availability of benchmark datasets such as CodeXGLUE can help the development and validation of new methods that can be applied to various program understanding and generation problems. The success of benchmark datasets such as ImageNet for computer vision and GLUE for natural language understanding has demonstrated the importance of diversified benchmark datasets in the growth of applied AI research [^2].

## Neuro-Symbolic Program Synthesis

Neuro-Symbolic Program Synthesis is a novel technique proposed to overcome the limitations of neural architectures for program induction [^3]. This technique can automatically construct computer programs in a domain-specific language that are consistent with a set of input-output examples provided at test time. The approach is based on two novel neural modules. The first module, called the cross-correlation I/O network, produces a continuous representation of the set of input-output examples. The second module, the Recursive-Reverse-Recursive Neural Network (R3NN), synthesizes a program by incrementally expanding partial programs. The R3NN model is not only able to construct programs from new input-output examples but also able to construct new programs for tasks that it had never observed before during training. This technique is motivated by the need for model interpretability and scalability to multiple tasks [^3].

### Background: This subsection provides a brief history of neural architectures for program induction and their limitations.

Recent years have seen the proposal of a number of neural architectures for the problem of Program Induction. These architectures are able to learn mappings that generalize to new test inputs. However, they have several limitations. Firstly, they are computationally expensive and hard to train. Secondly, a model has to be trained for each task (program) separately. Thirdly, it is hard to interpret or verify the correctness of the learnt mapping (as it is defined by a neural network) [^3]. These limitations have motivated the development of novel techniques such as Neuro-Symbolic Program Synthesis, which aims to overcome these problems and automatically construct computer programs in a domain-specific language that are consistent with a set of input-output examples provided at test time.

### Neuro-Symbolic Program Synthesis

Neuro-Symbolic Program Synthesis is a novel technique proposed by Parisotto et al. to overcome the limitations of neural architectures for program induction [^3]. The existing neural architectures for program induction are computationally expensive, hard to train, and require a separate model for each task. Moreover, it is difficult to interpret or verify the correctness of the learned mapping. Neuro-Symbolic Program Synthesis can automatically construct computer programs in a domain-specific language that are consistent with a set of input-output examples provided at test time. The proposed method is based on two novel neural modules: the cross-correlation I/O network and the Recursive-Reverse-Recursive Neural Network (R3NN). The cross-correlation I/O network produces a continuous representation of the set of input-output examples, while the R3NN synthesizes a program by incrementally expanding partial programs. The effectiveness of the approach is demonstrated by applying it to the domain of regular expression-based string transformations. The R3NN model is not only able to construct programs from new input-output examples but also able to construct new programs for tasks that it had never observed before during training [^3].

### Automatically Constructing Computer Programs

Neuro-Symbolic Program Synthesis is a novel technique proposed to overcome the limitations of neural architectures for program induction [^3]. The proposed technique can automatically construct computer programs in a domain-specific language that are consistent with a set of input-output examples provided at test time. The approach is based on two novel neural modules. The first module, called the cross correlation I/O network, produces a continuous representation of the set of input-output examples. The second module, the Recursive-Reverse-Recursive Neural Network (R3NN), synthesizes a program by incrementally expanding partial programs. The effectiveness of the approach has been demonstrated by applying it to the domain of regular expression based string transformations. The R3NN model is not only able to construct programs from new input-output examples but also able to construct new programs for tasks that it had never observed before during training [^3].

## Test Case Generation for Program Repair

This section investigates the feasibility and effectiveness of test case generation in alleviating the overfitting issue in test suite based program repair techniques. Test-suites are typically inadequate for completely specifying the expected behavior of the program under repair, which leads to overfitting patches that pass the test suite but may be incorrect. To address this issue, two approaches for using test case generation to improve test suite based repair are proposed in [^4]. The first approach works with generate-and-validate techniques (MinImpact), and the second one for synthesis-based techniques (UnsatGuided). The proposed approaches are evaluated on 224 bugs of the Defects4J repository, and the results indicate that test case generation can change the resulting patch, but is not effective at turning incorrect patches into correct ones. The study identifies the problems related to the ineffectiveness and anticipates that the findings will lead to future research to build test-case generation techniques that are tailored to automatic repair systems.

### Background: This subsection provides a brief history of program repair techniques and their limitations.

Program repair techniques aim to automatically fix software bugs. Among the many different kinds of program repair techniques, one widely studied family of techniques is called test suite based repair. Test-suites are in essence input-output specifications and are therefore typically inadequate for completely specifying the expected behavior of the program under repair. Consequently, the patches generated by test suite based program repair techniques pass the test suite, yet may be incorrect. Patches that are overly specific to the used test suite and fail to generalize to other test cases are called overfitting patches [^4]. The limitations of test suite based repair techniques have led to the investigation of the feasibility and effectiveness of test case generation in alleviating the overfitting issue.

### Feasibility and Effectiveness of Test Case Generation

Test suite based repair techniques suffer from the overfitting issue, where the generated patches may be overly specific to the used test suite and fail to generalize to other test cases. In order to alleviate this issue, test case generation has been proposed as a potential solution [^4]. This subsection investigates the feasibility and effectiveness of test case generation in improving test suite based repair techniques. The authors propose two approaches for using test case generation and perform an extensive evaluation on 224 bugs of the Defects4J repository. The results indicate that test case generation can change the resulting patch, but is not effective at turning incorrect patches into correct ones. The authors identify the problems related to the ineffectiveness and anticipate that their findings will lead to future research to build test-case generation techniques that are tailored to automatic repair systems [^4].

### Proposed Approaches for Using Test Case Generation

Test suite based repair techniques generate patches that pass the test suite but may be incorrect, leading to overfitting patches. In order to alleviate this issue, test case generation can be used to improve test suite based repair. Two approaches have been proposed for this purpose [^4]:

1. **MinImpact:** This approach is suitable for generate-and-validate techniques that can enumerate patches. It uses an evolutionary approach to derive test suites that maximize code coverage and generates assertions that encode the current behavior of the program. The aim is to use additional automatically generated tests to guide the patch generation process towards generating patches that are less likely to be overfitting.

2. **UnsatGuided:** This approach is suitable for synthesis-based techniques. It uses a constraint solver to synthesize patches that satisfy the given test suite. The aim is to use additional automatically generated tests to guide the synthesis process towards generating patches that are less likely to be overfitting.

These approaches have been evaluated on 224 bugs of the Defects4J repository, and the results indicate that test case generation can change the resulting patch, but is not effective at turning incorrect patches into correct ones. The ineffectiveness is attributed to the limitations of the generate-and-validate and synthesis-based techniques used in the study. Future research is anticipated to build test-case generation techniques that are tailored to automatic repair systems. [^4]

## Combinatorial Testing for Deep Learning Systems

Deep learning (DL) systems have been widely applied in various applications due to their high accuracy, but their robustness has recently received great concerns [^5]. Testing techniques could help to evaluate the robustness of a DL system and detect vulnerabilities at an early stage. However, the main challenge of testing such systems is that their runtime state space is too large [^5]. Combinatorial testing (CT) is an effective testing technique for traditional software to reduce the testing space while obtaining relatively high defect detection abilities. In an exploratory study of CT on DL systems, a set of coverage criteria for DL systems and a CT coverage guided test generation technique were proposed [^5]. The evaluation demonstrated that CT provides a promising avenue for testing DL systems. The proposed combinatorial testing coverage criteria are useful for adversarial example detection and local-robustness analysis [^5].

### Background: This subsection provides a brief history of deep learning systems and their challenges in testing.

Deep learning (DL) has achieved remarkable progress over the past decade and been widely applied to many safety-critical applications. However, the robustness of DL systems recently receives great concerns, such as adversarial examples against computer vision systems, which could potentially result in severe consequences [^5]. The main challenge of testing such systems is that its runtime state space is too large: if we view each neuron as a runtime state for DL, then a DL system often contains massive states, rendering testing each state almost impossible [^5].

### Combinatorial Testing

Combinatorial testing (CT) is a well-established and successful technique in traditional software testing that aims to reduce the testing space while obtaining relatively high defect detection abilities [^5]. CT focuses on testing the interactions of inputs rather than exhaustively searching all the combinations of input space. This technique has been successfully applied to testing different configurable software systems, as most faults are caused by interactions involving only a few parameters [^5]. However, CT is limited in handling various constraints and is not directly applicable to deep learning (DL) systems due to their massive runtime state space [^5]. 

In this paper, an exploratory study of CT on DL systems is performed. The concept of CT is adapted, and a set of coverage criteria for DL systems is proposed, as well as a CT coverage-guided test generation technique [^5]. The evaluation results demonstrate that CT provides a promising avenue for testing DL systems [^5].

### Coverage Criteria for Deep Learning Systems

Combinatorial testing (CT) has been proposed as a promising avenue for testing deep learning (DL) systems. To reduce the testing space while obtaining relatively high defect detection abilities, a set of coverage criteria for DL systems has been proposed [^5]. These criteria are useful for adversarial example detection and local-robustness analysis. The proposed CT coverage criteria have been evaluated on small-scale neural networks with only dense layers, with no more than 400 neurons. The usefulness and scalability of the proposed criteria have also been demonstrated on practical-sized DL systems such as ResNet-50 with near 200 layers and 100,000 neurons [^5].

## Conclusion

In this systematic review, we have explored the field of programming testing arxiv and its importance in solving the problem of software errors. We have covered five papers that discuss new approaches for generating test cases, benchmark datasets for machine learning research, novel techniques for program synthesis, feasibility and effectiveness of test case generation for program repair, and combinatorial testing for deep learning systems. 

Metamorphic testing has been proposed as a new approach for generating next test cases that can reveal software errors left undetected in successful test cases [^1]. CodeXGLUE has been introduced as a benchmark dataset for machine learning research in program understanding and generation, which can help accelerate research in programming language tasks [^2]. Neuro-symbolic program synthesis has been proposed as a novel technique to overcome the limitations of neural architectures for program induction [^3]. Test case generation for program repair has been investigated for its feasibility and effectiveness in alleviating the overfitting issue in test suite based program repair techniques [^4]. Combinatorial testing has been explored as a promising avenue for testing deep learning systems, and a set of coverage criteria for deep learning systems has been proposed [^5].

Future research directions in programming testing arxiv include exploring the potential of metamorphic testing in uncovering software errors in the production phase, developing new benchmark datasets for machine learning research, improving the effectiveness of test case generation for program repair, and further investigating the feasibility and effectiveness of combinatorial testing for deep learning systems. Overall, the papers covered in this systematic review provide valuable insights and directions for future research in programming testing arxiv. 

[^1]: 1. Metamorphic testing: a new approach for generating next test cases
[^2]: 2. Codexglue: A machine learning benchmark dataset for code understanding and generation
[^3]: 3. Neuro-symbolic program synthesis
[^4]: 4. Test case generation for program repair: A study of feasibility and effectiveness
[^5]: 5. Combinatorial testing for deep learning systems

## References
[^1]: [Chen, Tsong Y., Shing C. Cheung, and Shiu Ming Yiu. "Metamorphic testing: a new approach for generating next test cases." arXiv preprint arXiv:2002.12543 (2020).](https://arxiv.org/abs/2002.12543)

[^2]: [Lu, Shuai, et al. "Codexglue: A machine learning benchmark dataset for code understanding and generation." arXiv preprint arXiv:2102.04664 (2021).](https://arxiv.org/abs/2102.04664)

[^3]: [Parisotto, Emilio, et al. "Neuro-symbolic program synthesis." arXiv preprint arXiv:1611.01855 (2016).](https://arxiv.org/abs/1611.01855)

[^4]: [Yu, Zhongxing, et al. "Test case generation for program repair: A study of feasibility and effectiveness." arXiv preprint arXiv:1703.00198 (2017).](https://arxiv.org/abs/1703.00198)

[^5]: [Ma, Lei, et al. "Combinatorial testing for deep learning systems." arXiv preprint arXiv:1806.07723 (2018).](https://arxiv.org/abs/1806.07723)