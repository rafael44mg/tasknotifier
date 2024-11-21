TaskNotifier - Sistema de Notificação de Tarefas

Descrição
O TaskNotifier é um sistema de gerenciamento de tarefas que utiliza o padrão de projeto Observer para notificar os usuários sempre que o status de uma tarefa é alterado. O sistema é útil para cenários em que múltiplos usuários (gerentes, desenvolvedores, etc.) precisam ser informados sobre o progresso das tarefas em um fluxo de trabalho.

Padrão de Projeto: Observer
O padrão Observer é um padrão comportamental que permite que objetos (observadores) sejam notificados automaticamente sobre mudanças em outro objeto (sujeito). No TaskNotifier, o sujeito é a tarefa (Task), e os observadores são os usuários (Manager e Developer) que são notificados sempre que o status de uma tarefa muda.

Como Funciona
A classe Task (sujeito) mantém o estado das tarefas e notifica todos os observadores registrados quando o status da tarefa é alterado.
As classes Manager e Developer são implementações concretas do observador, que recebem notificações quando uma tarefa muda de status.
Quando o status de uma tarefa é alterado, os observadores são informados sobre a mudança e podem reagir de acordo com a lógica de seu tipo.

Tecnologias Usadas
Python 3.x
Padrão de Projeto Observer
Testes Unitários com unittest
logging para gerenciar logs e notificações

Estrutura do Projeto
task.py: Contém as classes que implementam o padrão Observer. Inclui a classe Task (sujeito) e os observadores Manager e Developer.
test_task.py: Contém os testes unitários para garantir que o sistema de notificações funcione corretamente. O teste verifica se os observadores são notificados corretamente quando o status de uma tarefa muda.

Como Usar

1. Instalar o Python
Certifique-se de ter o Python 3.x instalado. Você pode verificar se o Python está instalado no seu sistema com o comando:

bash

python --version

2. Rodar o Sistema
Clone ou baixe o repositório do projeto.
Navegue até o diretório do projeto.
Execute o código Python no terminal:

bash

python task.py

3. Rodar os Testes
Para rodar os testes unitários e verificar se o sistema de notificações está funcionando corretamente, execute o seguinte comando:

bash

python -m unittest test_task.py

O teste irá verificar se os observadores (gerente e desenvolvedor) são notificados corretamente quando o status das tarefas é alterado.

Explicação do Código
Task (Sujeito): A classe Task é o sujeito que mantém o estado da tarefa. Ela notifica todos os observadores registrados quando o status da tarefa é alterado.
User (Observador): A classe abstrata User define o método update que os observadores implementam para receber notificações.
Manager e Developer (Observadores): Essas são implementações concretas de observadores. Quando o status da tarefa muda, elas são notificadas e geram logs indicando a mudança de status.

Fluxo de Notificação:
Um usuário (como um gerente ou desenvolvedor) se registra para observar as tarefas.
Quando uma tarefa tem seu status alterado, o método notify_observers() é chamado, e todos os observadores são notificados com a nova informação do status.
O observador processa a mudança e executa ações baseadas no novo estado da tarefa.

Exemplo de Execução
Aqui está um exemplo simples de como a notificação funciona:

# Criando uma tarefa
task = Task("Implement feature X", "Develop the new feature for the project.")

# Criando observadores
manager = Manager("Alice")
developer = Developer("Bob")

# Registrando observadores na tarefa
task.add_observer(manager)
task.add_observer(developer)

# Alterando o status da tarefa, o que dispara as notificações
task.set_status("In Progress")
task.set_status("Completed")

Saída Esperada:
Durante a execução do código, você verá as mensagens de notificação sendo registradas no log, como:

INFO:task:Manager Alice is notified about the task 'Implement feature X' status change to In Progress.
INFO:task:Developer Bob is notified about the task 'Implement feature X' status change to In Progress.
INFO:task:Manager Alice is notified about the task 'Implement feature X' status change to Completed.
INFO:task:Developer Bob is notified about the task 'Implement feature X' status change to Completed.

Testes Unitários
Os testes garantem que o sistema de notificações esteja funcionando corretamente. Eles verificam se os observadores são notificados de maneira adequada sempre que o status de uma tarefa muda. O teste é executado com o comando:

bash

python -m unittest test_task.py

TaskNotifier é um exemplo prático de como implementar o padrão Observer em um sistema simples de gerenciamento de tarefas, garantindo que mudanças no estado da tarefa sejam corretamente comunicadas a todos os interessados.