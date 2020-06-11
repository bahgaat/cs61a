
; Tail recursion

(define (replicate x n)
  (define (helper n result)
    (if (= n 0)
      result
      (helper (- n 1) (append (cons x nil) result) )
    )
  )
  (helper n nil)
)

(define (accumulate combiner start n term)
  (if (= n 0)
    start
    (combiner (term n) (accumulate combiner start (- n 1) term))
  )
)

(define (accumulate-tail combiner start n term)
  (if (= n 0)
    start
   (accumulate-tail combiner (combiner start (term n)) (- n 1) term)
  )
)



; Streams

(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define multiples-of-three
  (cons-stream 3 (map-stream (lambda(x) (+ x 3)) multiples-of-three))
)


(define (nondecreastream s)
     (define (helper s counter r)
            (cond
              ((null? (cdr-stream s)) (cons-stream (list(car s)) nil))
              ((= counter 0) (cons-stream (cons(car s) (helper (cdr-stream s) (+ 1 counter) r)) (helper r counter (new-s r))))
              ((> (car s) (car (cdr-stream s))) (cons (car s) nil))
              (else  (cons (car s) (helper (cdr-stream s) (+ 1 counter) r)))
            )
      )
      (helper s 0 (new-s s))
)
(define (new-s s)
   (cond
       ((null? (cdr-stream s)) (cons-stream (list(car s)) nil))
       ((> (car s) (car (cdr-stream s))) (cdr-stream s))
       (else (new-s (cdr-stream s)))
    )
)


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))
