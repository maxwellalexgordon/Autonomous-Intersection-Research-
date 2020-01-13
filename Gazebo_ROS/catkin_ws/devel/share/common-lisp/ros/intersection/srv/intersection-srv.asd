
(cl:in-package :asdf)

(defsystem "intersection-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "CarComOne" :depends-on ("_package_CarComOne"))
    (:file "_package_CarComOne" :depends-on ("_package"))
    (:file "createCar" :depends-on ("_package_createCar"))
    (:file "_package_createCar" :depends-on ("_package"))
  ))