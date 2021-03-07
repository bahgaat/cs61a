(define-macro (switch expr cases)
     `(eval (car (cdr (car (filter (lambda (case) (equal? ,expr (car case))) ',cases )))))
    )


(define (flatmap f x)
  (define (helper k f x)
    (cond
      ((null? x) k)
      (else (helper (append k (f (car x)) ) f (cdr x)))
    )
  )
  (helper nil f x)
)

(define (g x)
  (cond
    ((equal? x 'x) '(x r y f r))
    ((equal? x 'y) '(l f x l y))
    (else (list x))
  )
)

(define (expand lst)
  (flatmap g lst)
)


(define (interpret instr dist)
  (cond
    ((null? instr) (fd 0))
    ((equal? (car instr) 'f) (begin (fd dist)  (interpret (cdr instr) dist)))
    ((equal? (car instr) 'l) (begin (lt 90) (interpret (cdr instr) dist)))
    ((equal? (car instr) 'r) (begin (rt 90)  (interpret (cdr instr) dist)))
    (else (interpret (cdr instr) dist))
  )
)


(define (apply-many n f x)
  (if (zero? n)
      x
      (apply-many (- n 1) f (f x))))

(define (dragon n d)
  (interpret (apply-many n expand '(f x)) d))


(define-macro (make-lambda expr)
    `(lambda () ,expr)
    )

(define (combine-with f xs ys)
  (if (or (null? xs) (null? ys))
    nil
    (cons-stream
    (f (car xs) (car ys))
    (combine-with f (cdr-stream xs) (cdr-stream ys)))))


(define-macro (while initial-bindings condition updates return)
    (define helper-vars
        (map (lambda(x)(car (cdr x))) initial-bindings))
    (define initial-vals
        (map (lambda(x)(car x)) initial-bindings))
        (list 'begin
            (list 'define (cons 'helper initial-vals)))
                `(if ,condition
                    (helper (map (lambda (x) x) ,updates))
                    ,return)
            (cons 'helper helper-vars))

  (define-macro (switch expr cases)
     `(eval (car (cdr (car (filter (lambda (x) (equal? ,expr (car x))) ',cases )))))
  )
