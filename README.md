# Minstrel

Minstrel is a multi-agent system for generating structured prompts in the LangGPT format. The project aims to improve the accuracy and diversity of generated text through collaboration between multiple intelligent agents to produce high-quality LangGPT prompts.

## News
- Minstrel is participating in the 4th Shusheng Large Model Training Camp
  ![Minstrel participating in the 4th Shusheng Large Model Training Camp](https://github.com/user-attachments/assets/5a32bd82-e2fd-4bdb-81ea-d5ff9fb648dd)

## Features

- Multi-agent collaboration for LangGPT prompt generation
- Efficient prompt generation algorithms
- Easy to extend and customize

## Installation

Please follow these steps to install and run the project:

1. Clone the repository:
    ```bash
    git clone https://github.com/sci-m-wang/Minstrel.git
    cd Minstrel
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    conda create -n langgpt python=3.10 -y
    conda activate langgpt
    ```

3. Install dependencies:
    ```bash
    pip install openai==1.37.1
    pip install streamlit==1.37.0
    ```

## Usage

Here's a simple example of how to use it:

1. Run the main script to generate LangGPT prompts:
    ```bash
    python -m streamlit run app.py
    ```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork this repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## Citation
If you use this project in your research, please cite the following papers:
```
@misc{wang2024langgptrethinkingstructuredreusable,
      title={LangGPT: Rethinking Structured Reusable Prompt Design Framework for LLMs from the Programming Language}, 
      author={Ming Wang and Yuanzhong Liu and Xiaoyu Liang and Songlian Li and Yijie Huang and Xiaoming Zhang and Sijia Shen and Chaofeng Guan and Daling Wang and Shi Feng and Huaiwen Zhang and Yifei Zhang and Minghui Zheng and Chi Zhang},
      year={2024},
      eprint={2402.16929},
      archivePrefix={arXiv},
      primaryClass={cs.SE},
      url={https://arxiv.org/abs/2402.16929}, 
}

@misc{wang2024minstrelstructuralpromptgeneration,
      title={Minstrel: Structural Prompt Generation with Multi-Agents Coordination for Non-AI Experts}, 
      author={Ming Wang and Yuanzhong Liu and Xiaoyu Liang and Yijie Huang and Daling Wang and Xiaocui Yang and Sijia Shen and Shi Feng and Xiaoming Zhang and Chaofeng Guan and Yifei Zhang},
      year={2024},
      eprint={2409.13449},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2409.13449}, 
}
```

## Contact

If you have any questions or suggestions, please contact us through:

- Email: sci.m.wang@gmail.com
- GitHub: [sci-m-wang](https://github.com/sci-m-wang)

## Star History

![Star History Chart](https://api.star-history.com/svg?repos=sci-m-wang/Minstrel&type=Date)

Thank you for using Minstrel!
