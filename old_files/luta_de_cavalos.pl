/*===========================================================================
 Jogo de Tabuleiro - Luta de Cavalos
==========================================================================*/

/*
 criar uma lista com os n.os interios de 0 a 99 e baralhar os elementos dessa lista
*/

%lista(+N,-L).
%devolve no segundo argumento uma lista com N inteiros por ordem decrescente
%a partir de N-1 at� 0.

lista(0,[]):-!.
lista(N,[A|Tail]):-
 A is N-1,
 lista(A,Tail).

%cria uma lista que representa o estado inicial do tabuleiro

cria_tabuleiro(Tab):-
 lista(100,TabOrdenado),
 shuffle(TabOrdenado,Tab),
 visualiza_estado(Tab),!.

/*esta ultima instrucaoo para teste apenas*/
%Transforma uma lista(com 100 elemento no caso em concreto)
%em listas com sublistas de 10 elementos e vise versa

lista_de_listas([],[]):-!.
lista_de_listas([A,B,C,D,E,F,G,H,I,J|Tail1],[[A,B,C,D,E,F,G,H,I,J]|Tail2]):-
 lista_de_listas(Tail1,Tail2).

/*baralha os elementos de uma lista*/
/*os dois predicados seguintes foram retirados de:
http://ozone.wordpress.com/2006/02/22/little-prolog-challenge/ */

%% shuffle(+ListIn,-ListOut) - randomly shuffles
%% ListIn and unifies it with ListOut

shuffle([], []).
shuffle(List, [Element|Rest]) :-
 choose(List, Element),
 delete(List, Element, NewList),
 shuffle(NewList, Rest).

 %% choose(+List,-Elt) - chooses a random element
%% in List and unifies it with Elt.

choose([], []).
choose(List, Elt) :-
 length(List, Length),
 random(0, Length, Index),
 nth0(Index, List, Elt).

visualiza_estado(Tabuleiro):-
 write(' Tabuleiro de Jogo '),nl,
 write(' Luta de Cavalos '),nl,
 write(' A B C D E F G H I J'),nl,
 write(' ______________________________'),nl,
 escreve(Tabuleiro,1),
 write(' ______________________________'),nl,
 write(' A B C D E F G H I J'),nl.
escreve([],_).
escreve([A,B,C,D,E,F,G,H,I,J|Tail],N):-
 N =< 10,
 M is N,
 write1(M),write(' |'),
 write1(A),write('|'),
 write1(B),write('|'),
 write1(C),write('|'),
 write1(D),write('|'),
 write1(E),write('|'),
write1(F),write('|'),
 write1(G),write('|'),
 write1(H),write('|'),
 write1(I),write('|'),
 write1(J),write('| '),write1(M),nl,
 escreve(Tail,M+1).
write1(X):-
 integer(X),
 X >= 10, write(X).
write1(X):-
 integer(X),
 X < 10, write('0'),write(X).
write1(X):-
 write(X).
%calcula o n�mero Y com dois algarismos que � o n�mero que resulta da troca dos
%dois algarimos do n�mero X. Se X tem apenas um algarismo o valor de Y ser� dez
%vezes o valor de X.
troca(X,Y):-
 X > 9,X < 100,
 DigitoUnidades is X mod 10,
 DigitoDezenas is (X-DigitoUnidades)/10,
 Y is DigitoDezenas+10*DigitoUnidades.
troca(X,Y):-
 X > 0,X =< 9,
 Y is X*10.
/*==========================================================================
 zona de testes
===========================================================================*/
%troca os algarismos de todos os elementos de uma lista
% n serve pra nada...
troca_lista([],[]).
troca_lista([X|Cauda1],[Y|Cauda2]):-
 troca(X,Y),
 troca_lista(Cauda1, Cauda2).
%predicado de teste que serve para apresentar o tabuleiro inicial
joga_teste:-
 cria_tabuleiro(_).
inicio:-
 cria_tabuleiro(Tab),
 primeira_jogada(Tab,Tab2),
 visualiza_estado(Tab2),
 lista_jogadas(Tab2,ListaJogadas),
 nl,write(ListaJogadas).
primeira_jogada([X|Tail1],[c1|Tail2]):-
 troca(X,Y),
 subst(Y,'##',Tail1,Tail2).
jogada(Coluna,Linha,Cavalo,Tab1,Tab2):-
 Pos is 10*(Linha-1)+(Coluna-1),
 nth0(Pos,Tab1,Num),
 subst(Num,Cavalo,Tab1,Tab3),
 troca(Num,NumTrocado),
 subst(NumTrocado,'##',Tab3,Tab2).
teste:-
 cria_tabuleiro(Tab),
 jogada(5,1,cb,Tab,Tab2),
 jogada(2,10,cp,Tab2,Tab3),
 subst(cb,'##',Tab3,Tab4),
 jogada(6,3,cb,Tab4,Tab5),
 subst(cp,'##',Tab5,Tab6),
 jogada(4,9,cp,Tab6,Tab7),
 subst(cb,'##',Tab7,Tab8),
 jogada(8,4,cb,Tab8,Tab9),
 visualiza_estado(Tab9).
/*substituir um n�mero X de uma lista por o atomo Y */
subst(_,_,[],[]):-!.
subst(X,Y,[Cab1|Tail1],[Cab1|Tail2]):-X \= Cab1, subst(X,Y,Tail1,Tail2).
subst(X,Y,[X|Tail1],[Y|Tail2]):- subst(X,Y,Tail1,Tail2).
lista_jogadas(Tab,ListaJogadas):-
 nth0(Pos,Tab,c1),
 P1 is Pos-8,P2 is Pos+8,
 P3 is Pos-12,P4 is Pos+12,
 P5 is Pos-19,P6 is Pos+19,
 P7 is Pos-21,P8 is Pos+21,
 L=[P1,P2,P3,P4,P5,P6,P7,P8],
 findall(X, (member(X,L),X >= 0,X < 100),ListaJogadas).






















