## Comparision Between Primitives:

| Lock Type           | Reentrancy | Concurrent Access Allowed      | Common Use Case                                                        |
|---------------------|------------|---------------------------------|------------------------------------------------------------------------|
| **Lock**            | No         | 1                               | Simple critical section protection.                                    |
| **RLock**           | Yes        | 1                               | Nested or recursive locking by the same thread.                        |
| **Semaphore**       | No         | N (defined by initial count)    | Limiting access to a pool of resources (e.g., database connections).   |
| **BoundedSemaphore**| No         | N (defined by initial count)    | Similar to `Semaphore`, but prevents exceeding initial count.          |
| **Condition**       | No         | N/A (based on waiting/notifying)| Coordination of complex states (e.g., producer-consumer pattern).       |

> Reentrancy refers to the ability of a lock to be acquired multiple times by the same thread without causing a deadlock. A reentrant lock allows the thread that currently holds the lock to re-acquire it.

> Concurrent Access Allowed: This refers to the number of threads that can simultaneously acquire a lock without blocking each other. It indicates how many threads can access a shared resource at the same time under the management of the lock.

> Note that, Semaphore and BoundedSemaphore both uses internal counter to manage the number of concurrent acquisitions.

**Semaphore and Bounded Semaphore:**

| Feature                   | Semaphore                       | BoundedSemaphore                  |
|---------------------------|---------------------------------|-----------------------------------|
| **Count Management**      | Unlimited (can exceed initial)  | Limited (cannot exceed initial)    |
| **Release Behavior**      | No error if released too many times | Raises `ValueError` if released too many times |
| **Use Case**             | General concurrent access control | Strict resource management and error prevention |