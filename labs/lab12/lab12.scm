(define (partial-sums stream)
  (define (helper i stream)
      (if (null? stream)
         nil
         (cons-stream (+ i (car stream)) (helper (+ i (car stream)) (cdr-stream stream)))))
  (helper 0 stream)
)
