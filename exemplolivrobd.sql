create schema exemplolivro;
use exemplolivro;

create table livro(
cd_livro int primary key not null auto_increment,
nome varchar (45),
lingua varchar (45),
ano int
);
create table editora(
cd_editora int primary key not null auto_increment,
nome varchar(45),
telefone varchar (16),
endereco varchar (100)
);
create table autor(
cd_autor int primary key not null auto_increment,
nome varchar (45),
dataNascimento date,
paisNascimento varchar (45),
notaBibliografica text
);
create table livro_autor(
cd_livro int not null,
cd_autor int not null, 
constraint foreign key (cd_livro) references livro(cd_livro), 
constraint foreign key (cd_autor) references autor(cd_autor)
);
create table edicao(
cd_edicao int primary key not null auto_increment,
ISBN varchar(45),
preco decimal(10,2),
ano int,
numPaginas int,
quantidade int,
cd_livro int null,
cd_editora int null,
constraint foreign key(cd_livro) references livro (cd_livro),
constraint foreign key (cd_editora) references editora (cd_editora)
);

