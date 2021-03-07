
(define-macro (switch expr cases)
     `(eval (car (cdr (car (filter (lambda (case) (equal? ,expr (car case))) ',cases )))))
    )

(define (cycle start)
    (let ((end (if (> (/ start 2) 1) (- start 3) (+ start 2)))) (cons-stream start (cycle end)))
)

(define (split s pred)
   (define (split-tail s result)
      (cond
         ((null? s) result)
         ((pred (car s)) (split-tail (cdr s)  (append (car result) (list (car s)))))
         (else (split-tail (cdr s)  (append (cdr result) (list (car s)))))
        )
    )
    (split-tail s '(() ()))
)
