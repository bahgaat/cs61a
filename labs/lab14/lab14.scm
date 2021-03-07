; Lab 14: Final Review

(define (compose-all funcs)
  (define (helper n)
    (define (helper-2 n funcs)
         (cond ((null? funcs) n)
               ((null? (cdr funcs)) ((car funcs) n))
               (else (helper-2 ((car funcs) n) (cdr funcs)))
          )
    )
    (helper-2 n funcs)
  )
  helper
)

(define (has-cycle? s)
  (define (pair-tracker seen-so-far curr)
    (cond (
          (else (pair-tracker (cdr-stream seen-so-far) seen-so-far))
    )
  )
  (pair-tracker (cdr-stream s) s)
)
)

(define (contains lst s)
  (cond ((null? lst) #f)
        ((eq? s (car lst)) #t)
        (else (contains (cdr lst) s))
    )
)

(define (cycle start)
    (let ((end (if (> (/ start 2) 1) (- start 3) (+ start 2)))) (cons-stream start (cdr-stream (cycle end))))
  )

  (define-macro (let-macro bindings body)
      (cons `(lambda ,(map car bindings) ,body) (map cadr bindings))
  )

(define-macro (zero-cond clauses)
    (cons 'cond
            (map  (lambda (clause) (if (> (eval (car clause)) 0) (list 'True (cadr clause)) (list 'False (cadr clause)))) clauses))

)

(define (pairs L)
    (define (accum_pairs lst result)
        (cond
           ((null? lst) result)
           ((null? (cdr lst)) (append result (cons lst nil)))
           (else (accum_pairs (cdr (cdr lst)) (append result (list (list (car lst) (car (cdr lst))))))))
    )
    (accum_pairs L nil)
)

(define-macro (partial call)
`(lambda (y) (cons (car ',call) (cdr ',call) (cons y nil))))
