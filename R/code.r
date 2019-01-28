setwd('~/DL-codes/R/')  # Set Working Directory
R.Version()
install.packages('dplyr')
library(dplyr)
?dplyr
?rnorm()
getwd()  # Get Working Directory  
library(tidyverse) # Call the Tidyverse package
install.packages('tidyverse') # Install it, if it's not there
senado <- read_csv("senado.csv") # read a csv file
head(senado) # head
tail(senado) # tail
str(senado)
class(senado)
summary(senado)
# Read a file where separation is given by #
read_delim('caminho/do/arquivo/arquivo_separado_por#.txt', delim = '#')
# Read a file whose separator is |
precos <- read_delim('TA_PRECOS_MEDICAMENTOS.csv', delim = '|')
head(precos)

# Read a fixed column file
read_fwf('fwf-sample.txt', col_positions = fwf_widths(c(20, 10, 12), c("nomes", "estado", "codigo")))
?read_csv
dim(senado)


# Defining vectors
vec.char <- c('char1', 'char2', 'char3', 'char4')
vec <- c(1,2,5,8,100)
vec
vec2 <- c(rep(2,50))
vec2
vec3 <- c(seq(from = 0, to = 100, by =5))
vec3

# Create a Dataframe from vectors

nome <- c('Jose', 'João', 'Pedro','Carlos')
idade <- c(45,12,28,31)
adulto <- c(TRUE, FALSE, TRUE, TRUE)
uf <- c('DF','SP','RJ', 'MG')

clientes <- data.frame(nome, idade, adulto, uf)
clientes
str(clientes)

data("airquality") # carrega uma base de dados pré-carregada no R
summary(airquality)
is.na(airquality$Ozone)


unique(senado$Party)
senado[72,]

senado[c(100, 200), c(2,3,4)] # selecionando mais de uma linha e coluna em um data.frame
senado[c(10:20), ]

