;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)

(define (sign x)
  (cond
    ((< x 0) -1)
    ((= x 0) 0)
    ((> x 0) 1)
  )
)

(define (square x) (* x x))

(define (pow b n)
  (cond
     ((= 1 n) b)
     ((even? n) (* b (pow b (- n 1))))
     ((odd? n) (* (square b) (pow b (- n 2))))
  )
)


(define (unique s)
    (if (null? s)
         nil
         (cons (car s) (unique (filter (lambda (x) (not (eq? x (car s)))) (cdr s))))
    )
)

(define (concat a b)
    (if (null? a)
        b
        (cons (car a)(concat (cdr a) b))
    )
)

(define (replicate x n)
    (if (= n 0)
        nil
        (cons x (replicate x (- n 1)))
    )
)

(define (uncompress s)
   (if (null? s)
        nil
        (concat (replicate (car(car s)) (car(cdr(car s)))) (uncompress (cdr s)))
   )
)

(define (map fn lst)
   (if (null? lst)
       nil
       (cons (fn (car lst)) (map fn (cdr lst)))))

(define (deep-apply fn nested-list)
    (cond
      ((null? nested-list) nil)
      ((list? (car nested-list)) (cons (deep-apply fn (car nested-list)) (deep-apply fn (cdr nested-list))))
      (else (cons (fn (car nested-list)) (deep-apply fn (cdr nested-list))))
    )
)

(define (make-tree root branches) (cons root branches))
(define (root tree) (car tree))
(define (branches tree) (cdr tree))

(define (tree-sum tree)
    (if (null? (branches tree))
         (root tree)
         (+ (root tree)(reduce + (map tree-sum (branches tree))))
    )
)

(define (path-product-tree tree)
   (define (helper tree previous_root)
      (if (null? (branches tree))
         (make-tree (* (root tree) previous_root )  nil)
         (make-tree (* (root tree) previous_root ) ( map (lambda(b) (helper b (* previous_root (root tree)))) (branches tree)))
      )
    )
    (helper tree 1)
)

(define (sixty-ones list)
  (cond
    ((null? list) 0)
    ((and (= (car list) 6) (= (car(cdr list)) 1)) (+ 1 (sixty-ones (cddr list))))
    (else (sixty-ones (cdr list)))
  )
)

(define (no-eleven n)
   (cond
      ((= n 1) (list (list 6)(list 1)))
      (else (append (map (lambda(b) (append '(6) b)) (no-eleven(- n 1))) (let ((x (filter (lambda(b) (not(= (car b) 1))) (no-eleven(- n 1)))))
            (map (lambda(b) (append '(1) b)) x))))
    )
)


(define (better-append (variadic x))
   (cond
        ((null? x) nil)
        ((null? (cdr x)) (car x))
        (else  (concat (car x) (better-append (car(cdr x)) (cddr x) ) ) ) 
    )
)
