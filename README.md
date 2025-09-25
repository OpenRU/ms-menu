#  Microsserviço de Gestão de Cardápios Diários

Este microsserviço é responsável por gerenciar cardápios diários de forma simples e organizada.  
Permite criar, visualizar, atualizar e excluir cardápios para datas específicas, garantindo consistência e facilidade de consulta.

##  Funcionalidades

- Criar cardápio para uma data específica.
- Visualizar cardápio(s) cadastrados.
- Atualizar cardápio existente.
- Excluir cardápio.
- Consultar o cardápio do **dia atual** via endpoint.

##  Estrutura do Cardápio

Cada cardápio deve conter os seguintes campos obrigatórios:

- **Data** (DD-MM-AAAA)  
- **Prato Principal**  
- **Guarnição**  
- **Salada**  
- **Sobremesa**  
- **Bebida**

##  Regras de Negócio

- Não pode existir **mais de um cardápio** para a mesma data.
- Todos os campos são obrigatórios.
- A data deve estar em formato válido (`DD-MM-AAAA`).
