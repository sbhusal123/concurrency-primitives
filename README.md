# Python Concurrency Primitives:

Some of the reference can be found on the [Book](./book.pdf) starting from page number: 307 on concurrency.

## Section1:

This section covers the very basics of the threading, multiprocessing, memory and program architecture.

- [1. Threads And MultiThreading](./References/Section1/1.%20Thread%20and%20Multithreading.md)
    - Intro To Threads
    - Multiple Threads
    - Multithreading Advantages and Disadvantages

- [2. Processes and Event Driven Programming](./References/Section1/2.%20Processes%20and%20Event%20Driven%20Programming.md)
    - Intro To Processes
    - Properties of Process
    - Advantages and Disadvantages of Multiprocessing
    - Illustration Of Event Driven Program

- [3. Threads Vs Sequential Execution: Example](./References/Section1/3.%20ImageDownloaderComparision.md)
    - Sequentual and Threaded implementation for image downloader

- [4. Improving Computation with Multiprocessing: Comparision and Example with Sequential Approach](./References/Section1/4.%20Improving%20Computation%20With%20MultiProcessing.md)
    - Sequential and Multiprocessing approach for prime factorization

- [5. Concurrency And Parallelism, Bottlenecks](./References/Section1/5.%20Concurrency%20and%20IO%20bottleneck.md)
    - Concurrency
    - Properties of Concurrent System
    - IO Bottlenecks

- [6. Parallelism](./References/Section1/6.%20Parallelism.md)
    - Parallelism
    - Concurrency Vs Parallelism
    - CPu Bound Bottlenecks

- [7. Memory Architecture](./References/Section1/7.%20Memory%20Architecture.md)
    - Unified Memory Access
    - Non Unified Memory Access

- [8. Threading in Python](./References/Section1/Threads%20In%20Python/)

    - [8.1. Intro To Thread in Python](./References/Section1/Threads%20In%20Python/1.%20Threads%20in%20Python.md)
        - Python threading module constructor params.
        - Thread States
        - Thread State Transition, Example with Code

    - [8.2. Starting A Thread](./References/Section1/Threads%20In%20Python/2.%20Starting%20A%20Thread.md)
        - Class Based Initialization Of Thread
        - Process Forking, Example
        - Daemon Thread, Usage, Example
    
    - [8.3. Handling Threads in Python](./References/Section1/Threads%20In%20Python/3.%20Handling%20threads.md)
        - Listing active threads objects: ``threading.enumerate()``
        - Get current thread: ``threading.current_thread()``
        - Main Thread: Program Thread: ``threading.main_thread()``
        - Thread naming: ``threading.current_thread().name``, construct thread name initialization.

- [9. Synchronization Primitives](./References/Section1/Threads%20In%20Python/Synchronization%20Primitive/)

    - [9.1. Comparision Between Different Primitives](./References/Section1/Threads%20In%20Python/Synchronization%20Primitive/Comparision%20Between%20Primitives.md)
        - Tabular Comparision: Lock, RLock, Semaphore, BoundedSemaphore
        - Semaphore Vs BoundedSemaphore

    - [9.2. Deadlock and Race Condition](./References/Section1/Threads%20In%20Python/Synchronization%20Primitive/DeadLock%20and%20Race%20Condition.md)

    - [9.2. Synchronization Between Threads](./References/Section1/Threads%20In%20Python/Synchronization%20Primitive/Synchronization%20Between%20Threads.md)
        - Dining philosopher problem

    - [9.3. Shared Resource And Data Race](./References/Section1/Threads%20In%20Python/Synchronization%20Primitive/Shared%20Resource%20And%20Data%20Race.md)
        - threading.Lock
        - threading.RLock
        - Lock vs RLock

    - [9.4. Conditions](./References/Section1/Threads%20In%20Python/Synchronization%20Primitive//Condition.md)
        - Example Illustration with pseudocode in C.
        - Key Concepts For Pythonic Implementation
        - Condition class method.
        - Example Implementation with python.

    - [9.5. Semaphores](./References/Section1/Threads%20In%20Python/Synchronization%20Primitive//Semaphore.md)

    - [9.6. BoundedSemaphore](./References/Section1/Threads%20In%20Python/Synchronization%20Primitive/BoundedSemaphore.md)

    - [9.7. Event](./References/Section1/Threads%20In%20Python/Synchronization%20Primitive/Events.md)

    - [9.8. Barriers](./References/Section1/Threads%20In%20Python/Synchronization%20Primitive/Barriers.md)
