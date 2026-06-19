;; BtcL2Demo — 教学 Clarity 合约模板，仅测试网

(define-data-var counter uint u0)

(define-public (increment)
  (ok (var-set counter (+ (var-get counter) u1))))

(define-read-only (get-counter)
  (ok (var-get counter)))
