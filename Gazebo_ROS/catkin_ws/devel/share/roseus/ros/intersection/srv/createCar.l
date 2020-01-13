;; Auto-generated. Do not edit!


(when (boundp 'intersection::createCar)
  (if (not (find-package "INTERSECTION"))
    (make-package "INTERSECTION"))
  (shadow 'createCar (find-package "INTERSECTION")))
(unless (find-package "INTERSECTION::CREATECAR")
  (make-package "INTERSECTION::CREATECAR"))
(unless (find-package "INTERSECTION::CREATECARREQUEST")
  (make-package "INTERSECTION::CREATECARREQUEST"))
(unless (find-package "INTERSECTION::CREATECARRESPONSE")
  (make-package "INTERSECTION::CREATECARRESPONSE"))

(in-package "ROS")





(defclass intersection::createCarRequest
  :super ros::object
  :slots (_check ))

(defmethod intersection::createCarRequest
  (:init
   (&key
    ((:check __check) 0)
    )
   (send-super :init)
   (setq _check (round __check))
   self)
  (:check
   (&optional __check)
   (if __check (setq _check __check)) _check)
  (:serialization-length
   ()
   (+
    ;; int64 _check
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _check
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _check (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _check) (= (length (_check . bv)) 2)) ;; bignum
              (write-long (ash (elt (_check . bv) 0) 0) s)
              (write-long (ash (elt (_check . bv) 1) -1) s))
             ((and (class _check) (= (length (_check . bv)) 1)) ;; big1
              (write-long (elt (_check . bv) 0) s)
              (write-long (if (>= _check 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _check s)(write-long (if (>= _check 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _check
#+(or :alpha :irix6 :x86_64)
      (setf _check (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _check (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(defclass intersection::createCarResponse
  :super ros::object
  :slots (_vin _speed _accel _enterTime _lane _turn _length _width ))

(defmethod intersection::createCarResponse
  (:init
   (&key
    ((:vin __vin) 0)
    ((:speed __speed) 0.0)
    ((:accel __accel) 0.0)
    ((:enterTime __enterTime) 0)
    ((:lane __lane) 0)
    ((:turn __turn) 0)
    ((:length __length) 0.0)
    ((:width __width) 0.0)
    )
   (send-super :init)
   (setq _vin (round __vin))
   (setq _speed (float __speed))
   (setq _accel (float __accel))
   (setq _enterTime (round __enterTime))
   (setq _lane (round __lane))
   (setq _turn (round __turn))
   (setq _length (float __length))
   (setq _width (float __width))
   self)
  (:vin
   (&optional __vin)
   (if __vin (setq _vin __vin)) _vin)
  (:speed
   (&optional __speed)
   (if __speed (setq _speed __speed)) _speed)
  (:accel
   (&optional __accel)
   (if __accel (setq _accel __accel)) _accel)
  (:enterTime
   (&optional __enterTime)
   (if __enterTime (setq _enterTime __enterTime)) _enterTime)
  (:lane
   (&optional __lane)
   (if __lane (setq _lane __lane)) _lane)
  (:turn
   (&optional __turn)
   (if __turn (setq _turn __turn)) _turn)
  (:length
   (&optional __length)
   (if __length (setq _length __length)) _length)
  (:width
   (&optional __width)
   (if __width (setq _width __width)) _width)
  (:serialization-length
   ()
   (+
    ;; int64 _vin
    8
    ;; float64 _speed
    8
    ;; float64 _accel
    8
    ;; int64 _enterTime
    8
    ;; int64 _lane
    8
    ;; int64 _turn
    8
    ;; float64 _length
    8
    ;; float64 _width
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _vin
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _vin (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _vin) (= (length (_vin . bv)) 2)) ;; bignum
              (write-long (ash (elt (_vin . bv) 0) 0) s)
              (write-long (ash (elt (_vin . bv) 1) -1) s))
             ((and (class _vin) (= (length (_vin . bv)) 1)) ;; big1
              (write-long (elt (_vin . bv) 0) s)
              (write-long (if (>= _vin 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _vin s)(write-long (if (>= _vin 0) 0 #xffffffff) s)))
     ;; float64 _speed
       (sys::poke _speed (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _accel
       (sys::poke _accel (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; int64 _enterTime
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _enterTime (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _enterTime) (= (length (_enterTime . bv)) 2)) ;; bignum
              (write-long (ash (elt (_enterTime . bv) 0) 0) s)
              (write-long (ash (elt (_enterTime . bv) 1) -1) s))
             ((and (class _enterTime) (= (length (_enterTime . bv)) 1)) ;; big1
              (write-long (elt (_enterTime . bv) 0) s)
              (write-long (if (>= _enterTime 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _enterTime s)(write-long (if (>= _enterTime 0) 0 #xffffffff) s)))
     ;; int64 _lane
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _lane (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _lane) (= (length (_lane . bv)) 2)) ;; bignum
              (write-long (ash (elt (_lane . bv) 0) 0) s)
              (write-long (ash (elt (_lane . bv) 1) -1) s))
             ((and (class _lane) (= (length (_lane . bv)) 1)) ;; big1
              (write-long (elt (_lane . bv) 0) s)
              (write-long (if (>= _lane 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _lane s)(write-long (if (>= _lane 0) 0 #xffffffff) s)))
     ;; int64 _turn
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _turn (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _turn) (= (length (_turn . bv)) 2)) ;; bignum
              (write-long (ash (elt (_turn . bv) 0) 0) s)
              (write-long (ash (elt (_turn . bv) 1) -1) s))
             ((and (class _turn) (= (length (_turn . bv)) 1)) ;; big1
              (write-long (elt (_turn . bv) 0) s)
              (write-long (if (>= _turn 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _turn s)(write-long (if (>= _turn 0) 0 #xffffffff) s)))
     ;; float64 _length
       (sys::poke _length (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _width
       (sys::poke _width (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _vin
#+(or :alpha :irix6 :x86_64)
      (setf _vin (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _vin (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; float64 _speed
     (setq _speed (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _accel
     (setq _accel (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; int64 _enterTime
#+(or :alpha :irix6 :x86_64)
      (setf _enterTime (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _enterTime (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _lane
#+(or :alpha :irix6 :x86_64)
      (setf _lane (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _lane (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _turn
#+(or :alpha :irix6 :x86_64)
      (setf _turn (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _turn (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; float64 _length
     (setq _length (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _width
     (setq _width (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass intersection::createCar
  :super ros::object
  :slots ())

(setf (get intersection::createCar :md5sum-) "81fafe211a05479f18572c2a83d88d33")
(setf (get intersection::createCar :datatype-) "intersection/createCar")
(setf (get intersection::createCar :request) intersection::createCarRequest)
(setf (get intersection::createCar :response) intersection::createCarResponse)

(defmethod intersection::createCarRequest
  (:response () (instance intersection::createCarResponse :init)))

(setf (get intersection::createCarRequest :md5sum-) "81fafe211a05479f18572c2a83d88d33")
(setf (get intersection::createCarRequest :datatype-) "intersection/createCarRequest")
(setf (get intersection::createCarRequest :definition-)
      "int64 check
---
int64 vin
float64 speed
float64 accel
int64 enterTime
int64 lane
int64 turn
float64 length
float64 width

")

(setf (get intersection::createCarResponse :md5sum-) "81fafe211a05479f18572c2a83d88d33")
(setf (get intersection::createCarResponse :datatype-) "intersection/createCarResponse")
(setf (get intersection::createCarResponse :definition-)
      "int64 check
---
int64 vin
float64 speed
float64 accel
int64 enterTime
int64 lane
int64 turn
float64 length
float64 width

")



(provide :intersection/createCar "81fafe211a05479f18572c2a83d88d33")


