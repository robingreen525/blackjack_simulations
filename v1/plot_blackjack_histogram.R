require(ggplot2)
setwd('X:/fast/shou_w/shougroup/lab_users/Robin/Robin_Code/blackjack/')
r<-read.csv('money.txt',header=F)

#r<-r[1]
colnames(r)<-c('Money','Ignore')

g<-ggplot(data=r,aes(x=Money,))+geom_histogram(binwidth=10,aes(fill=..count..))+
  scale_fill_gradient('Count',low='green',high='red')+
  geom_vline(xintercept = mean(r$Money))
print(g)