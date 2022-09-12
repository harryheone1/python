# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# get several subjects of a single document
def extract_subjects(document_txt):
    return document_txt


thales_general_work_map = {'AI_Architect': [], 'CD4ML': [], 'MLOps': [],
                           'Container': ['Docker', 'Kubernetes'],
                           '机器学习项目的坑': [],
                           'time_series': ['time', 'series'],
                           'location_predict': ['location'],
                           'ethic_AI': ['differential', 'privacy', 'federated', 'fairness'],
                           'SVD': ['奇异值', '特征值', 'eigen', 'svd', 'matrix'],
                           'recommendation_system': ['recommendation', 'recommended', 'collaborative'],
                           'EDA_FE_POC_steps': ['EDA', 'exploratory', 'feature'],
                           'anomaly_detection': ['anomaly', 'outlier'],
                           'confidence_learning': ['remediation', 'GAN', 'confidence'],
                           'attack_ML': ['attack'],
                           'graph_similarity': [],
                           'causal_inference': ['probabilistic', 'causal'],
                           'NLP': ['language'],
                           'User_profiling': ['behavior'],
                           'Segmentation': ['clustering'],
                           'Authentication': ['login', 'Koaclock'],
                           'model_explainer': ['shap'],
                           'knowledge_graph': [], 'semi_supervised': [], 'transfer_learning': [],
                           'adaptive_learning': [],
                           'Scrapy': []}

personal_improvement_map = {'ML_base_udacity': [],
                            'statistic': ['统计学的大道感悟'],
                            'ml_white_board': ['白板推公式和及其理论基础'],
                            'python': ['Python基础和数学编程'],
                            'reputation': [],
                            'ml_basic': ['机器学习快速入门和机器学习系统设计'],
                            'dl_basic': ['深度学习快速入门'],
                            'nlp_udacity': ['NLP实践课程'],
                            'leadership': ['项目和团队管理'],
                            'probability': [],
                            'linear_algebra': [], 'calculus': [],
                            'cs_basic': ['CS基本概念'], 'cs_tools': ['编程工具使用'],
                            '技术兴衰+跌宕起伏': [], 'jb_hire_info': [],
                            'algorithm': ['算法和数据结构'], 'distribute_architect': ['分布式架构'],
                            'AWS_cloud': [], 'RL_udacity': [],
                            'business_to_model': ['如何根据业务建立统计模型和数学模型'],
                            'AI_application': [], 'communication': [], 'work_experience': [],
                            'interview_experience': [],
                            'career_development': [],
                            'tensorflow_pytorch': [],
                            'distribute_embedded_ml': [],
                            'spark_functional': ['functional', 'scala'],
                            'ml_interview': [],
                            'programming_paradigm': [],
                            'optimization_or': ['最优化和OR'],
                            'reinforcement': [], 'new_research': ['paper'],
                            'backend_bigdata': [],
                            'computer_vision': [],
                            'game': [], 'bigdata_from_0': [], 'phd': [], 'kaggle': []}

thales_specific_work_map = {'SEA_Architect', 'network_knowledge', 'product_roadmap', 'Container', '机器学习项目的坑',
                            'AIQ_paper', 'ProactiveOps', 'network_common_data_model', 'STC_Bouyegues', 'SIQ'}

manual_promote_map = {
    '项目管理，总体把握和Presentation': '',
    'NLP': 'nlp_udacity',
}

# Press the green button in the gutter to run the script.
# 中英文词汇对应
# 词根匹配忽略特殊字符
if __name__ == '__main__':
    print_hi('PyCharm')
    subjects = extract_subjects('')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
