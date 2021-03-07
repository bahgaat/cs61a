;; Scheme ;;

(define (over-or-under x y)
  (cond
    ((< x y) -1)
    ((= x y) 0)
    ((> x y) 1))
)

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0

(define (filter-lst f lst)
  (cond
    ((null? lst) nil)
    ((f (car lst)) (cons (car lst) (filter-lst f (cdr lst))))
    (else (filter-lst f (cdr lst)))
  )
)

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)

(define (make-adder num)
  (define (adder x)
    (+ num x))
  adder
)


;;; Tests
(define adder (make-adder 5))
(adder 8)
; expect 13

;; Extra questions

(define lst
  (list (list 1) 2 (list 3 4) 5)
)

(define (composed f g)
  (define (new_compose x)
    (f(g x)))
  new_compose
)

(define (remove item lst)
  (cond
    ((null? lst) nil)
    ((= item (car lst))(remove item (cdr lst)))
    (else (cons (car lst)(remove item (cdr lst))))
  )
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

(define (no-repeats s)
  (define (new_list l s)
    (if (null? s)
        l
       (remove(car s) l)(set-car! l (car s))(new_list (l)(cdr s))))
  (new_list nil s)
)

(define (substitute s old new)
  (if (null? s)
    nil
    (if (pair? (car s))
       (cons (substitute (car s) old new) (substitute (cdr s) old new))
       (if (equal? (car s) old)
         (cons new (substitute (cdr s) old new))
         (cons (car s) (substitute (cdr s) old new))
      )
    )
  )
)


(define (sub-all s olds news)
  (cond
     ((null? s) nil)
     ((null? olds) (cons (car s) (sub-all (cdr s) olds news)))
     (else (cons (car(sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news))) (sub-all (cdr s) olds news)))
  )
)
