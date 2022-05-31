from graphics import *
import time
import math
def main():
	inicio=GraphWin("iniciar", 960, 720)
	menu=Image(Point(480,360), "Menu.png")
	menu.draw(inicio)
	new=Image(Point(430,330), "New Game.png")
	new.draw(inicio)
	P1=Image(Point(875,545), "mago.png")
	esq1=Image(Point(630,680),"SkeletonWalking.gif")
	esq2=Image(Point(630,530), "SkeletonWalking.gif")
	boss=Image(Point(450,250), "Verminor_boss.png")
	bar=Image(Point(480,360), "bar_room.png")
	cidade=Image(Point(480,360), "Cidade.png")
	entrada=Image(Point(480,360), "dungeon_entry.png")
	dungeon=Image(Point(480,360), "dentro calabouço.png")	
	salafinal=Image(Point(480,360), "Final_Boss.png")
	perdedor=Image(Point(480,360), "loser.png")
	vencedor=Image(Point(480,360), "Winner.png")
	Mapas=["bar", "cidade", "entrada", "dungeon", "salafinal"]
	
	i=0
	p=0
	PI=0
	PF=0
	PR=0
	PR2=0
	VP=1
	VPB=0.3
	AP=None
	AB=None
	PIB=0
	PFB=0
	PRB=0
	vx=0
	vy=0
	bx=0
	by=0
	vb=15
	vm=5
	
	if inicio.getMouse():
		menu.undraw()
		new.undraw()
	while True:
		mover=inicio.checkKey()
		PF = inicio.checkMouse()
		if (PF != None):
			PI=P1.getAnchor()
			AP=Image(PI, "ataque mago.png")
			AP.draw(inicio)
			PR=(PF.x-PI.x , PF.y-PI.y)
			vx = PR[0]/math.sqrt(PR[0]**2+PR[1]**2)
			vy = PR[1]/math.sqrt(PR[0]**2+PR[1]**2)
			#PR1= PF.x - PI.x
			#PR2= PF.y - PI.y
		if AP !=None:
			AP.move(vx*VP, vy*VP)
			if AP.getAnchor().x ==inicio.checkMouse() and AP.getAnchor.y ==inicio.checkMouse():
				if AP.getAnchor().x>960 or AP.getAnchor().x<10 or AP.getAnchor().y>720 or AP.getAnchor().y<10:
					AP.undraw()
					AP=None
				
		if(mover!="Escape"):
			if P1.getAnchor().y>20:
				if mover=="Up":
					P1.move(0,-3)
			if P1.getAnchor().y<700:
				if mover=="Down":
					P1.move(0,3)
			if P1.getAnchor().x>20:	
				if mover=="Left":
					P1.move(-3,0)
			if P1.getAnchor().x<950:	
				if mover=="Right":
					P1.move(3,0)


			
		if i==0:
			if p==0:
				bar.draw(inicio)
				P1.draw(inicio)
				p=1	
			if P1.getAnchor().x==950 and P1.getAnchor().y>100 and P1.getAnchor().y<600:
				p=0
				i=1	
		if i==1:
			if p==0:
				bar.undraw()
				P1.undraw()
				cidade.draw(inicio)
				P1=Image(Point(270,170), "mago.png")
				P1.draw(inicio)
				print("erro")
				p=1
			if P1.getAnchor().y==680 and P1.getAnchor().x>100 and P1.getAnchor().x<600:
				p=0
				i=2
				#if de fim de mapa: i=i+1
		if i==2:
			if p==0:
				cidade.undraw()
				P1.undraw()
				entrada.draw(inicio)
				P1=Image(Point(480,50), "mago.png")
				P1.draw(inicio)
				p=1
			if P1.getAnchor().y>680 and P1.getAnchor().x>100 and P1.getAnchor().x<600:
				p=0
				i=3
				#if de fim de mapa: i=i+1
		if i==3:
			if p==0:
				entrada.undraw()
				P1.undraw()
				dungeon.draw(inicio)
				P1=Image(Point(30,600), "mago.png")
				P1.draw(inicio)
				esq1.draw(inicio)
				esq2.draw(inicio)
				p=1
			if P1.getAnchor().y<200 and P1.getAnchor().x>800 and P1.getAnchor().x<960:
				p=0
				i=4
				#if de fim de mapa: i=i+1
		if i==4:	
			if p==0:
				esq1.undraw()
				esq2.undraw()
				dungeon.undraw()
				P1.undraw()
				salafinal.draw(inicio)
				P1=Image(Point(475,600), "mago.png")
				P1.draw(inicio)
				boss.draw(inicio)	
				
				p=1 
			#print("boss1")

			if AB==None:
				AB=Image(Point(450,250), "boss cortado.png")
				AB.draw(inicio)
				#print("boss2")
				PIB= boss.getAnchor()
				PFB= P1.getAnchor()
				PRB=(PFB.x-PIB.x , PFB.y-PIB.y)
				bx = PRB[0]/math.sqrt(PRB[0]**2+PRB[1]**2)
				by = PRB[1]/math.sqrt(PRB[0]**2+PRB[1]**2)				
				#print("bosss2")
			if AB!=None:
				#print("boss3")
				AB.move(bx*VPB, by*VPB)
				if AB.getAnchor().x>960 or AB.getAnchor().x<10 or AB.getAnchor().y>720 or AB.getAnchor().y<10:
					AB.undraw()
					AB=None
			if AB!=None:
				#print("boss4")
				C1=AB.getAnchor()
				C2=Point(AB.getAnchor().x+AB.getWidth(), AB.getAnchor().y+AB.getHeight())
				D1=P1.getAnchor()
				D2=Point(P1.getAnchor().x+P1.getWidth(), P1.getAnchor().y+P1.getHeight())
				if ((C1.x>D1.x and C1.x<D2.x) or (C2.x>D1.x and C2.x<D2.x)) and ((C1.y>D1.y and C1.y<D2.y) or (C2.y>D1.y and C2.y<D2.y)):
					vm=vm-1
					AB.undraw()
					AB=None
			if AP!=None:
				A1=AP.getAnchor()
				#print(A1)
				A2=Point(AP.getAnchor().x+AP.getWidth(), AP.getAnchor().y+AP.getHeight())
				#print(AP.getWidth())
				#print(A2)
				B1=boss.getAnchor()
				#print(B1)
				B2=Point(boss.getAnchor().x+boss.getWidth(), boss.getAnchor().y+boss.getHeight())
				#print(B2)
				
				if ((A1.x>B1.x and A1.x<B2.x) or (A2.x>B1.x and A2.x<B2.x)) and ((A1.y > B1.y and A1.y<B2.y) or (A2.y> B1.y and A2.y<B2.y)):	
					
					vb=vb-1
					AP.undraw()
					AP=None
				if vb == 0:
					boss.undraw()
					salafinal.undraw()
					i=5
					p=0
				if vm == 0:
					P1.undraw()
					salafinal.undraw()
					i=6
					p=0
			
		if i==5:
			if p==0:	
				vencedor.draw(inicio)
				p=1
		if i==6:
			if p==0:
				perdedor.draw(inicio)
				p=1
	inicio.getMouse()
	inicio.close()
main()	
######COMENTARIO
'''Nesta primeira semana, tentei botar tudo que precisava botar no jogo para depois só trabalhar em coisas um pouco mais complexas, nas proximas semanas, respectivamente, pretendo botar a movimentação, arrumar a posição dos personagens e mexer nos "ataques" de todos bonecos, e na ultima pretendo acrescentar a colisão, tanto de ataque quanto pra andar para os bonecos não se atravessarem e não atravessarem as paredes.'''
#####COMENTARIO
	
	
	
	
	
	
	
	
	
	
	
