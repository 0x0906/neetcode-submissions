## Phase 1: Core Java — The Non-Negotiable Foundation (Weeks 1–4)

### 1.1 Language Fundamentals

| Topic | What You Must Know |
|---|---|
| **JDK vs JRE vs JVM** | JDK = Development Kit (javac + JRE). JRE = Runtime (JVM + libraries). JVM = Virtual Machine that executes bytecode. |
| **Data Types** | Primitives (`int`, `long`, `float`, `double`, `boolean`, `char`, `byte`, `short`) vs Wrapper Classes (`Integer`, `Long`, `Float`, `Double`, `Boolean`, `Character`). Autoboxing/Unboxing. |
| **String** | `String` is immutable. `StringBuilder` (not thread-safe, fast) vs `StringBuffer` (thread-safe, slower). String Pool. Why `==` fails and `.equals()` works. `String.format()`, `String.join()`. |
| **Arrays** | Declaration, initialization, multi-dimensional arrays. `Arrays.sort()`, `Arrays.copyOf()`, `Arrays.asList()`. |
| **Type Casting** | Widening (automatic: `int` → `long`) vs Narrowing (explicit: `double` → `int`). Upcasting/Downcasting with objects. |
| **Operators** | Arithmetic, relational, logical, bitwise (`&`, `|`, `^`, `~`, `<<`, `>>`), ternary (`? :`), `instanceof`. |
| **Control Flow** | `if/else`, `switch` (including enhanced switch with `->` in Java 14+), `for`, `for-each`, `while`, `do-while`, `break`, `continue`, labeled breaks. |

### 1.2 Object-Oriented Programming (OOP)
| Concept | What You Must Know | Interview Trap |
|---|---|---|
| **Class & Object** | Class = blueprint. Object = instance. Constructors (default, parameterized, copy). `this` keyword. | "Can a constructor be private?" → Yes (Singleton pattern). |
| **Encapsulation** | Private fields + public getters/setters. Data hiding. | "Why not just make everything public?" → Breaks invariants, no validation. |
| **Inheritance** | `extends` keyword. Single inheritance only (classes). `super` keyword. Constructor chaining. Method overriding (`@Override`). | "Does Java support multiple inheritance?" → Not with classes. Yes with interfaces (since Java 8). |
| **Polymorphism** | **Compile-time** (method overloading — same name, different params). **Runtime** (method overriding — parent reference, child object). | "Can you override a static method?" → No. It's method hiding, not overriding. |
| **Abstraction** | `abstract` classes (0–100% abstraction) vs `interface` (100% abstraction, but can have `default` and `static` methods since Java 8). | "When to use abstract class vs interface?" → Abstract class = IS-A with shared state. Interface = CAN-DO capability contract. |
| **Association** | Aggregation (HAS-A, weak — Department has Students, students exist independently). Composition (HAS-A, strong — House has Rooms, rooms don't exist without the house). | Know the UML difference. |

### 1.3 Key Java Packages & Classes You Must Know

```
java.lang       → String, StringBuilder, Math, System, Object, Thread, Runnable,
                   Comparable, Iterable, Exception, RuntimeException, Wrapper classes
java.util       → List, ArrayList, LinkedList, Set, HashSet, TreeSet, LinkedHashSet,
                   Map, HashMap, TreeMap, LinkedHashMap, Queue, Deque, ArrayDeque,
                   PriorityQueue, Collections, Arrays, Optional, Iterator, Comparator,
                   Objects, UUID, Date (legacy), Calendar (legacy)
java.util.stream → Stream, Collectors, IntStream, LongStream
java.time        → LocalDate, LocalTime, LocalDateTime, ZonedDateTime, Duration,
                   Period, Instant, DateTimeFormatter (NEVER use java.util.Date in new code)
java.io          → File, FileReader, FileWriter, BufferedReader, BufferedWriter,
                   InputStream, OutputStream, Serializable, ObjectInputStream,
                   ObjectOutputStream
java.nio         → Path, Paths, Files, ByteBuffer (modern file I/O)
java.net         → URL, HttpURLConnection (basic), Socket, ServerSocket
java.sql         → Connection, Statement, PreparedStatement, ResultSet, DriverManager
java.util.concurrent → ExecutorService, Executors, Future, CompletableFuture,
                        CountDownLatch, CyclicBarrier, Semaphore, ConcurrentHashMap,
                        AtomicInteger, ReentrantLock, BlockingQueue
```

### 1.4 Collections Framework (CRITICAL — Asked in Every Interview)

```
                     Collection (interface)
                     /        |         \
                List       Set         Queue
               / | \      / | \        / \
     ArrayList  |  Vector  HashSet  |   PriorityQueue  ArrayDeque
        LinkedList     TreeSet  LinkedHashSet

                     Map (interface) — NOT part of Collection
                    / | \
            HashMap  TreeMap  LinkedHashMap
                |
         ConcurrentHashMap
```

| Collection | Ordering | Duplicates | Null | Thread-Safe | When to Use |
|---|---|---|---|---|---|
| `ArrayList` | Insertion order | Yes | Yes | No | Default list. Random access by index. |
| `LinkedList` | Insertion order | Yes | Yes | No | Frequent insertions/deletions in the middle. Also implements `Deque`. |
| `HashSet` | No order | No | 1 null | No | Fast lookup, uniqueness check. |
| `LinkedHashSet` | Insertion order | No | 1 null | No | Unique + maintain insertion order. |
| `TreeSet` | Sorted (natural/comparator) | No | No null | No | Sorted unique elements. |
| `HashMap` | No order | Keys: No, Values: Yes | 1 null key | No | Default key-value store. O(1) get/put. |
| `LinkedHashMap` | Insertion order | Keys: No, Values: Yes | 1 null key | No | Ordered key-value. Good for LRU caches. |
| `TreeMap` | Sorted by key | Keys: No, Values: Yes | No null key | No | Sorted key-value. |
| `ConcurrentHashMap` | No order | Keys: No, Values: Yes | No nulls | Yes | Thread-safe map. Preferred over `Hashtable`. |
| `PriorityQueue` | Heap order (min by default) | Yes | No | No | Processing elements by priority. |
| `ArrayDeque` | Insertion order | Yes | No | No | Stack (LIFO) or Queue (FIFO). Faster than `Stack` and `LinkedList`. |

**Key methods to know:** `add()`, `remove()`, `contains()`, `get()`, `put()`, `keySet()`, `values()`, `entrySet()`, `size()`, `isEmpty()`, `iterator()`, `stream()`.

**`Comparable` vs `Comparator`:**
- `Comparable<T>` → Implement `compareTo(T o)` inside the class. Natural ordering. One way to sort.
- `Comparator<T>` → Implement `compare(T o1, T o2)` externally. Multiple ways to sort. Used with `Collections.sort(list, comparator)` or `list.sort(comparator)`.

### 1.5 Exception Handling

```
              Throwable
              /       \
         Error       Exception
      (Don't catch)    /       \
                Checked    RuntimeException (Unchecked)
             /    |    \       /    |    \    \
   IOException  SQL  Class   NullPointer  ArrayIndex  ClassCast  IllegalArgument
            Exception  NotFoundException  Exception  OutOfBounds  Exception   Exception
```

| Concept | What You Must Know |
|---|---|
| `try-catch-finally` | `finally` always executes (except `System.exit()`). |
| `try-with-resources` | `try (Resource r = new Resource()) { }` — auto-closes `AutoCloseable` resources. **Always use this for I/O.** |
| Checked vs Unchecked | Checked = compiler forces you to handle (`IOException`). Unchecked = runtime errors (`NullPointerException`). |
| Custom Exceptions | `class MyException extends RuntimeException { }` — create domain-specific exceptions. |
| `throw` vs `throws` | `throw` = manually throw an exception. `throws` = declare in method signature. |

### 1.6 Java 8+ Features (Interviewers Love This)

| Feature | Syntax / Example | Why It Matters |
|---|---|---|
| **Lambda Expressions** | `(a, b) -> a + b` | Concise anonymous functions. Replaces verbose anonymous classes. |
| **Functional Interfaces** | `@FunctionalInterface` — has exactly one abstract method. Built-in: `Predicate<T>`, `Function<T,R>`, `Consumer<T>`, `Supplier<T>`, `BiFunction<T,U,R>`, `UnaryOperator<T>`, `BinaryOperator<T>` | Foundation of lambdas and streams. |
| **Stream API** | `list.stream().filter().map().collect()` | Declarative data processing. Replaces for-loops for transformations. |
| **Key Stream Ops** | `filter()`, `map()`, `flatMap()`, `reduce()`, `collect()`, `forEach()`, `sorted()`, `distinct()`, `limit()`, `skip()`, `count()`, `findFirst()`, `findAny()`, `anyMatch()`, `allMatch()`, `noneMatch()`, `toList()` (Java 16+) | |
| **Collectors** | `Collectors.toList()`, `Collectors.toSet()`, `Collectors.toMap()`, `Collectors.groupingBy()`, `Collectors.partitioningBy()`, `Collectors.joining()`, `Collectors.counting()` | Terminal operations for streams. |
| **Optional** | `Optional.of()`, `Optional.ofNullable()`, `Optional.empty()`, `.isPresent()`, `.ifPresent()`, `.orElse()`, `.orElseThrow()`, `.map()`, `.flatMap()` | Eliminates `NullPointerException`. **Used heavily in Spring Data JPA.** |
| **Method References** | `ClassName::methodName` — e.g., `System.out::println`, `String::toUpperCase`, `MyClass::new` | Cleaner lambda syntax. |
| **Default Methods** | `default void myMethod() { }` in interfaces | Allows adding methods to interfaces without breaking implementations. |
| **`var` (Java 10+)** | `var list = new ArrayList<String>();` | Local variable type inference. |
| **Records (Java 16+)** | `record User(String name, int age) {}` | Immutable data classes with auto-generated `equals()`, `hashCode()`, `toString()`, getters. |
| **Sealed Classes (Java 17)** | `sealed class Shape permits Circle, Rectangle {}` | Restricts which classes can extend. |
| **Pattern Matching** | `if (obj instanceof String s) { s.length(); }` | Eliminates redundant casting. |
| **Text Blocks (Java 15+)** | `"""multi-line string"""` | Clean multi-line strings (great for SQL, JSON). |

### 1.7 Generics

| Concept | Example |
|---|---|
| Generic Class | `class Box<T> { T value; }` |
| Generic Method | `<T> T getFirst(List<T> list) { }` |
| Bounded Types | `<T extends Comparable<T>>` — T must implement Comparable |
| Wildcards | `?` (unknown), `? extends T` (upper bound — read), `? super T` (lower bound — write). **PECS: Producer Extends, Consumer Super.** |
| Type Erasure | Generics are compile-time only. At runtime, `List<String>` becomes `List<Object>`. |

### 1.8 Multithreading & Concurrency

| Concept | What You Must Know |
|---|---|
| **Thread Creation** | `extends Thread` vs `implements Runnable` (preferred) vs `implements Callable<V>` (returns value). |
| **Thread Lifecycle** | New → Runnable → Running → Blocked/Waiting/Timed_Waiting → Terminated. |
| **`synchronized`** | Keyword for mutual exclusion. Can be on methods or blocks. Intrinsic lock (monitor). |
| **`volatile`** | Ensures visibility of changes across threads. Does NOT guarantee atomicity. |
| **`wait()` / `notify()` / `notifyAll()`** | Inter-thread communication. Must be called inside `synchronized` block. |
| **ExecutorService** | `Executors.newFixedThreadPool(n)`, `Executors.newCachedThreadPool()`, `Executors.newSingleThreadExecutor()`. Submit tasks with `submit()`. Shutdown with `shutdown()`. |
| **Future & CompletableFuture** | `Future<T>` — blocking result. `CompletableFuture<T>` — non-blocking, chainable: `.thenApply()`, `.thenAccept()`, `.thenCompose()`, `.thenCombine()`, `.exceptionally()`, `.allOf()`, `.anyOf()`. |
| **Thread-safe Collections** | `ConcurrentHashMap`, `CopyOnWriteArrayList`, `BlockingQueue` (`LinkedBlockingQueue`, `ArrayBlockingQueue`). |
| **Atomic Classes** | `AtomicInteger`, `AtomicLong`, `AtomicReference` — lock-free thread-safe operations. |
| **Locks** | `ReentrantLock` (more flexible than `synchronized`), `ReadWriteLock`, `StampedLock`. |
| **Deadlock** | Two threads waiting for each other's locks. Prevention: consistent lock ordering, `tryLock()` with timeout. |

### 1.9 Java Memory Model (Interview Favorite)

```
JVM Memory:
├── Heap (shared across threads)
│   ├── Young Generation
│   │   ├── Eden Space (new objects created here)
│   │   ├── Survivor Space S0
│   │   └── Survivor Space S1
│   └── Old Generation (long-lived objects promoted here)
├── Stack (per thread — stores method frames, local variables, references)
├── Metaspace (class metadata — replaced PermGen in Java 8)
├── Program Counter Register (per thread)
└── Native Method Stack (per thread)
```

| Concept | What You Must Know |
|---|---|
| **Stack vs Heap** | Stack: local variables, method calls (fast, thread-private). Heap: objects (shared, GC-managed). |
| **Garbage Collection** | Automatic memory management. GC types: Serial, Parallel, G1 (default in Java 9+), ZGC (low latency). You don't control *when* GC runs. `System.gc()` is a suggestion, not a command. |
| **`finalize()`** | Deprecated. Don't use it. Use `try-with-resources` or `Cleaner`. |
| **Memory Leaks in Java** | Yes, they exist. Common causes: unclosed resources, static collections growing forever, inner class holding outer class reference, forgotten listeners/callbacks. |

---

## Phase 2: Build Tools & Project Structure (Week 5)

### 2.1 Maven (Industry Standard Build Tool)

| Concept | What You Must Know |
|---|---|
| **`pom.xml`** | Project Object Model. The central config file. |
| **GAV Coordinates** | `groupId` (org), `artifactId` (project name), `version`. |
| **Dependencies** | Added inside `<dependencies>`. Maven downloads them from Maven Central. |
| **Dependency Scope** | `compile` (default), `provided` (available at compile, not packaged — e.g., Servlet API), `test` (only for tests — e.g., JUnit), `runtime` (not needed at compile, needed at runtime — e.g., JDBC driver). |
| **Lifecycle Phases** | `clean` → `validate` → `compile` → `test` → `package` → `verify` → `install` → `deploy`. |
| **Key Commands** | `mvn clean install`, `mvn clean package`, `mvn dependency:tree`, `mvn spring-boot:run`. |
| **Plugins** | `maven-compiler-plugin`, `maven-surefire-plugin` (runs tests), `spring-boot-maven-plugin` (creates fat JAR). |
| **BOM (Bill of Materials)** | `<dependencyManagement>` section. Spring Boot Starter Parent is a BOM that manages all version numbers for you. |

### 2.2 Project Structure (Standard Layout)

```
my-project/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/mycompany/myproject/
│   │   │       ├── MyProjectApplication.java        # Main class (@SpringBootApplication)
│   │   │       ├── config/                           # Configuration classes
│   │   │       ├── controller/                       # REST Controllers
│   │   │       ├── service/                          # Business Logic
│   │   │       ├── repository/                       # Data Access (JPA Repos)
│   │   │       ├── model/ (or entity/ or domain/)    # Entity classes
│   │   │       ├── dto/                              # Data Transfer Objects
│   │   │       ├── exception/                        # Custom exceptions & handlers
│   │   │       ├── mapper/                           # Entity ↔ DTO mappers
│   │   │       └── util/                             # Utility/helper classes
│   │   └── resources/
│   │       ├── application.yml (or .properties)      # App configuration
│   │       ├── application-dev.yml                   # Dev profile config
│   │       ├── application-prod.yml                  # Prod profile config
│   │       └── db/migration/                         # Flyway SQL migrations
│   └── test/
│       └── java/
│           └── com/mycompany/myproject/               # Mirror of main structure
├── pom.xml
├── Dockerfile
├── docker-compose.yml
├── .gitignore
└── README.md
```

### 2.3 Git (Version Control — Non-Negotiable)

| Command | Purpose |
|---|---|
| `git init` | Initialize a repo |
| `git clone <url>` | Clone a remote repo |
| `git add .` | Stage all changes |
| `git commit -m "message"` | Commit staged changes |
| `git push origin main` | Push to remote |
| `git pull origin main` | Pull latest changes |
| `git branch feature/xyz` | Create a branch |
| `git checkout feature/xyz` | Switch to branch |
| `git merge feature/xyz` | Merge branch into current |
| `git rebase main` | Rebase current branch onto main |
| `git stash` / `git stash pop` | Temporarily save uncommitted changes |
| `git log --oneline -n 10` | View recent commit history |
| `git diff` | See uncommitted changes |
| `.gitignore` | Exclude files: `target/`, `*.class`, `.env`, `*.log`, `.idea/`, `*.iml` |

**Branching Strategy:** `main` (stable) → `develop` (integration) → `feature/xxx` (individual features). Use meaningful commit messages.

---

## Phase 3: SQL & Database (Weeks 5–6)

> [!IMPORTANT]
> SQL is tested in **every single backend interview** in India. If you can't write a JOIN query or design a normalized schema, you will be rejected regardless of your Java skills.

### 3.1 PostgreSQL (Recommended) or MySQL

| Topic | What You Must Know |
|---|---|
| **DDL** | `CREATE TABLE`, `ALTER TABLE` (ADD/DROP/MODIFY COLUMN), `DROP TABLE`, `TRUNCATE`. |
| **DML** | `INSERT INTO`, `UPDATE ... SET ... WHERE`, `DELETE FROM ... WHERE`, `SELECT`. |
| **Constraints** | `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL`, `CHECK`, `DEFAULT`. |
| **Data Types** | `INT/BIGINT`, `VARCHAR(n)`, `TEXT`, `BOOLEAN`, `DATE`, `TIMESTAMP`, `DECIMAL/NUMERIC`, `UUID`, `JSONB` (PostgreSQL). |
| **SELECT Mastery** | `WHERE`, `AND/OR/NOT`, `IN`, `BETWEEN`, `LIKE` (`%` and `_`), `IS NULL / IS NOT NULL`, `ORDER BY`, `LIMIT/OFFSET`, `DISTINCT`, `CASE WHEN ... THEN ... ELSE ... END`. |
| **JOINs** | `INNER JOIN`, `LEFT JOIN` (LEFT OUTER), `RIGHT JOIN`, `FULL OUTER JOIN`, `CROSS JOIN`, `SELF JOIN`. **Practice these until you can write them in your sleep.** |
| **Aggregate Functions** | `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`. Used with `GROUP BY` and `HAVING`. |
| **Subqueries** | Scalar subquery, column subquery, correlated subquery, `EXISTS`, `IN (SELECT ...)`. |
| **Window Functions** | `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `LEAD()`, `LAG()`, `SUM() OVER(PARTITION BY ...)`. **This is an advanced differentiator.** |
| **Indexing** | B-Tree (default), single-column, composite (multi-column), `UNIQUE INDEX`. Know WHEN to create indexes (frequently queried columns, JOIN columns, WHERE clause columns) and their trade-offs (slower writes). `EXPLAIN ANALYZE` to check query plans. |
| **Normalization** | 1NF (atomic values), 2NF (no partial dependency), 3NF (no transitive dependency). Know when to denormalize for performance. |
| **Transactions** | `BEGIN`, `COMMIT`, `ROLLBACK`. ACID properties (Atomicity, Consistency, Isolation, Durability). Isolation levels: `READ UNCOMMITTED`, `READ COMMITTED` (PostgreSQL default), `REPEATABLE READ`, `SERIALIZABLE`. |
| **Views** | `CREATE VIEW view_name AS SELECT ...` — virtual table for complex queries. |

### 3.2 Database Design Interview Questions

Practice designing schemas for:
- E-commerce (Users, Products, Orders, OrderItems, Payments, Reviews)
- Social media (Users, Posts, Comments, Likes, Followers)
- Banking (Accounts, Transactions, Customers, Branches)

---

## Phase 4: Spring Framework & Spring Boot (Weeks 6–12)

> [!NOTE]
> **Spring Framework** = The core dependency injection and configuration framework.
> **Spring Boot** = An opinionated, auto-configured wrapper around Spring that eliminates boilerplate XML configuration.

### 4.1 Spring Core Concepts

| Concept | What It Means |
|---|---|
| **IoC (Inversion of Control)** | The framework controls object creation and lifecycle, not you. |
| **DI (Dependency Injection)** | Objects receive their dependencies from the outside (Spring container) rather than creating them. |
| **Spring Container / ApplicationContext** | The IoC container that manages all Spring beans. |
| **Bean** | Any object managed by the Spring container. |
| **Auto-wiring** | Spring automatically injects dependencies by type. |

### 4.2 All Spring Boot Annotations You Must Know

#### Core / Configuration Annotations

| Annotation | Where | Purpose |
|---|---|---|
| `@SpringBootApplication` | Main class | Combines `@Configuration` + `@EnableAutoConfiguration` + `@ComponentScan`. Entry point. |
| `@Configuration` | Class | Declares a class as a source of bean definitions. |
| `@Bean` | Method (inside `@Configuration`) | Registers the method's return value as a Spring bean. |
| `@Component` | Class | Generic stereotype annotation. Marks class as Spring-managed bean. |
| `@Service` | Class | Specialization of `@Component` for business logic layer. |
| `@Repository` | Class | Specialization of `@Component` for data access layer. Enables exception translation. |
| `@Controller` | Class | Specialization of `@Component` for MVC web controllers (returns views). |
| `@RestController` | Class | `@Controller` + `@ResponseBody`. Returns data (JSON), not views. **Use this for APIs.** |
| `@ComponentScan` | Class | Tells Spring which packages to scan for components. |
| `@Autowired` | Field/Constructor/Setter | Injects a dependency. **Constructor injection is preferred.** |
| `@Qualifier("name")` | Field/Parameter | Disambiguates when multiple beans of same type exist. |
| `@Primary` | Class/Method | Marks a bean as the default when multiple candidates exist. |
| `@Value("${property.name}")` | Field | Injects a value from `application.yml` / `application.properties`. |
| `@ConfigurationProperties(prefix = "app")` | Class | Binds a group of properties to a POJO. Type-safe configuration. |
| `@Profile("dev")` | Class/Method | Activates a bean only for a specific profile. |
| `@Scope("prototype")` | Class | Defines bean scope: `singleton` (default — one instance), `prototype` (new instance each time), `request`, `session`. |
| `@Lazy` | Class/Field | Bean is created only when first requested, not at startup. |
| `@PostConstruct` | Method | Runs after bean is created and dependencies are injected. |
| `@PreDestroy` | Method | Runs before bean is destroyed. |
| `@ConditionalOnProperty` | Class/Method | Creates bean only if a property exists/matches. |
| `@EnableScheduling` | Configuration class | Enables `@Scheduled` methods. |
| `@Scheduled(cron = "...")` | Method | Runs a method on a schedule. |
| `@Async` | Method | Executes the method asynchronously in a separate thread. |
| `@EnableAsync` | Configuration class | Enables `@Async` support. |

#### Web / REST Annotations

| Annotation | Where | Purpose |
|---|---|---|
| `@RequestMapping("/api")` | Class/Method | Maps HTTP requests to handler methods. Base path for a controller. |
| `@GetMapping("/users")` | Method | Handles `GET` requests. |
| `@PostMapping("/users")` | Method | Handles `POST` requests. |
| `@PutMapping("/users/{id}")` | Method | Handles `PUT` requests (full update). |
| `@PatchMapping("/users/{id}")` | Method | Handles `PATCH` requests (partial update). |
| `@DeleteMapping("/users/{id}")` | Method | Handles `DELETE` requests. |
| `@PathVariable` | Parameter | Extracts value from URL path: `/users/{id}` → `@PathVariable Long id`. |
| `@RequestParam` | Parameter | Extracts query parameter: `/users?name=John` → `@RequestParam String name`. |
| `@RequestBody` | Parameter | Deserializes JSON request body into a Java object. |
| `@ResponseBody` | Method/Class | Serializes return value to JSON response body. (Included in `@RestController`). |
| `@ResponseStatus(HttpStatus.CREATED)` | Method/Class | Sets the HTTP status code of the response. |
| `@CrossOrigin` | Class/Method | Enables Cross-Origin Resource Sharing (CORS). |
| `@RequestHeader` | Parameter | Extracts an HTTP header value. |

#### Validation Annotations (from `jakarta.validation`)

| Annotation | Purpose |
|---|---|
| `@Valid` | Triggers validation on a `@RequestBody` parameter. |
| `@NotNull` | Field must not be null. |
| `@NotBlank` | String must not be null, empty, or whitespace. |
| `@NotEmpty` | Collection/String must not be null or empty. |
| `@Size(min = 2, max = 50)` | String/Collection size constraints. |
| `@Min(1)` / `@Max(100)` | Numeric minimum/maximum value. |
| `@Email` | Must be a valid email format. |
| `@Pattern(regexp = "...")` | Must match a regex pattern. |
| `@Positive` / `@PositiveOrZero` | Must be a positive number. |
| `@Past` / `@Future` | Date must be in the past/future. |

#### JPA / Hibernate Annotations

| Annotation | Purpose |
|---|---|
| `@Entity` | Marks a class as a JPA entity (database table). |
| `@Table(name = "users")` | Specifies the table name. |
| `@Id` | Marks the primary key field. |
| `@GeneratedValue(strategy = GenerationType.IDENTITY)` | Auto-generates ID. Strategies: `IDENTITY` (database auto-increment), `SEQUENCE`, `UUID`, `AUTO`. |
| `@Column(name = "...", nullable = false, unique = true, length = 255)` | Maps a field to a specific column with constraints. |
| `@Enumerated(EnumType.STRING)` | Stores enum as a string (not ordinal). **Always use STRING.** |
| `@Temporal(TemporalType.TIMESTAMP)` | For legacy `java.util.Date` fields. Not needed with `java.time` classes. |
| `@CreatedDate` | Auto-populates creation timestamp. Requires `@EnableJpaAuditing`. |
| `@LastModifiedDate` | Auto-populates last modification timestamp. |
| `@OneToOne` | One-to-one relationship. |
| `@OneToMany(mappedBy = "parent")` | One-to-many relationship. `mappedBy` = the field in the child entity. |
| `@ManyToOne` | Many-to-one relationship. Usually paired with `@JoinColumn`. |
| `@ManyToMany` | Many-to-many relationship. Uses a join table. |
| `@JoinColumn(name = "user_id")` | Specifies the foreign key column. |
| `@JoinTable` | Configures the join table for `@ManyToMany`. |
| `@Transient` | Field is NOT persisted to the database. |
| `@Lob` | Large object (for storing large text or binary data). |
| **Fetch Types** | `FetchType.LAZY` (load on access — default for collections, **preferred**) vs `FetchType.EAGER` (load immediately — default for `@ManyToOne`). |
| **Cascade Types** | `CascadeType.ALL`, `.PERSIST`, `.MERGE`, `.REMOVE`, `.REFRESH`, `.DETACH`. Controls how operations propagate to related entities. |

#### Transaction Annotations

| Annotation | Purpose |
|---|---|
| `@Transactional` | Wraps a method in a database transaction. Rolls back on unchecked exceptions by default. |
| `@Transactional(readOnly = true)` | Optimizes read-only queries (no dirty checking). |
| `@Transactional(propagation = ...)` | `REQUIRED` (default — join existing or create new), `REQUIRES_NEW` (always create new), `SUPPORTS`, `MANDATORY`, `NEVER`, `NOT_SUPPORTED`, `NESTED`. |
| `@Transactional(isolation = ...)` | Controls isolation level for the transaction. |
| `@Transactional(rollbackFor = Exception.class)` | Explicitly rolls back for checked exceptions. |

### 4.3 Spring Data JPA (Data Access Layer)

**Repository Interfaces:**

```java
// Basic CRUD
public interface UserRepository extends JpaRepository<User, Long> {

    // Derived query methods — Spring generates SQL from method name
    Optional<User> findByEmail(String email);
    List<User> findByLastNameAndAge(String lastName, int age);
    List<User> findByAgeBetween(int min, int max);
    List<User> findByNameContainingIgnoreCase(String keyword);
    List<User> findByStatusOrderByCreatedAtDesc(Status status);
    boolean existsByEmail(String email);
    long countByStatus(Status status);
    void deleteByEmail(String email);

    // Custom JPQL query
    @Query("SELECT u FROM User u WHERE u.age > :age AND u.status = :status")
    List<User> findActiveUsersOlderThan(@Param("age") int age,
                                        @Param("status") Status status);

    // Native SQL query
    @Query(value = "SELECT * FROM users WHERE email LIKE %:domain", nativeQuery = true)
    List<User> findByEmailDomain(@Param("domain") String domain);

    // Pagination and Sorting
    Page<User> findByStatus(Status status, Pageable pageable);
    // Called with: userRepo.findByStatus(Status.ACTIVE, PageRequest.of(0, 10, Sort.by("name")));
}
```

**Repository Hierarchy:**
```
Repository (marker interface)
  └── CrudRepository (basic CRUD: save, findById, findAll, delete, count)
        └── ListCrudRepository
              └── PagingAndSortingRepository (adds Pageable + Sort support)
                    └── JpaRepository (adds flush, saveAll, batch operations)
```

### 4.4 Spring Boot Starters (Key Dependencies)

| Starter | Purpose |
|---|---|
| `spring-boot-starter-web` | REST APIs, embedded Tomcat, Jackson JSON |
| `spring-boot-starter-data-jpa` | JPA + Hibernate ORM |
| `spring-boot-starter-validation` | Bean validation (`@Valid`, `@NotNull`, etc.) |
| `spring-boot-starter-security` | Authentication & Authorization |
| `spring-boot-starter-test` | JUnit 5 + Mockito + MockMvc |
| `spring-boot-starter-actuator` | Health checks, metrics, monitoring endpoints |
| `spring-boot-starter-cache` | Caching abstraction |
| `spring-boot-starter-mail` | Email sending |
| `spring-boot-starter-aop` | Aspect-Oriented Programming support |
| `spring-boot-devtools` | Hot reload during development |

### 4.5 `application.yml` Configuration You Must Know

```yaml
server:
  port: 8080

spring:
  application:
    name: my-service

  # Database
  datasource:
    url: jdbc:postgresql://localhost:5432/mydb
    username: ${DB_USERNAME}          # Read from environment variable
    password: ${DB_PASSWORD}
    driver-class-name: org.postgresql.Driver

  # JPA / Hibernate
  jpa:
    hibernate:
      ddl-auto: validate             # Options: none, validate, update, create, create-drop
    show-sql: true
    properties:
      hibernate:
        format_sql: true
        dialect: org.hibernate.dialect.PostgreSQLDialect

  # Profiles
  profiles:
    active: dev                       # Activates application-dev.yml

  # Flyway (Database Migration)
  flyway:
    enabled: true
    locations: classpath:db/migration

# Logging
logging:
  level:
    root: INFO
    com.mycompany.myproject: DEBUG
    org.hibernate.SQL: DEBUG
```

### 4.6 Exception Handling (Global)

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(ResourceNotFoundException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public ErrorResponse handleNotFound(ResourceNotFoundException ex) {
        return new ErrorResponse("NOT_FOUND", ex.getMessage());
    }

    @ExceptionHandler(MethodArgumentNotValidException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public ErrorResponse handleValidation(MethodArgumentNotValidException ex) {
        Map<String, String> errors = new HashMap<>();
        ex.getBindingResult().getFieldErrors()
           .forEach(e -> errors.put(e.getField(), e.getDefaultMessage()));
        return new ErrorResponse("VALIDATION_FAILED", errors.toString());
    }

    @ExceptionHandler(Exception.class)
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    public ErrorResponse handleGeneral(Exception ex) {
        return new ErrorResponse("INTERNAL_ERROR", "Something went wrong");
    }
}
```

### 4.7 DTO Pattern & MapStruct

**Why DTOs:** Never expose your `@Entity` directly to the API. Use Data Transfer Objects to:
- Control what data is exposed (security)
- Decouple API contract from database schema
- Handle request/response shaping independently

```java
// Request DTO
public record CreateUserRequest(
    @NotBlank String name,
    @Email @NotBlank String email,
    @Min(18) int age
) {}

// Response DTO
public record UserResponse(
    Long id,
    String name,
    String email,
    LocalDateTime createdAt
) {}
```

**MapStruct (recommended for Entity ↔ DTO mapping):**
```java
@Mapper(componentModel = "spring")
public interface UserMapper {
    UserResponse toResponse(User user);
    User toEntity(CreateUserRequest request);
}
```

### 4.8 Spring Security Basics

| Concept | What You Must Know |
|---|---|
| **Authentication** | Verifying WHO the user is. (Username/password, JWT, OAuth2) |
| **Authorization** | Verifying WHAT the user can do. (Roles, permissions) |
| **SecurityFilterChain** | The chain of filters that process every HTTP request. |
| **BCryptPasswordEncoder** | Hash passwords. Never store plain text. |
| **JWT (JSON Web Token)** | Stateless authentication token. Structure: `Header.Payload.Signature`. Used with `Authorization: Bearer <token>` header. |
| **`@PreAuthorize("hasRole('ADMIN')")`** | Method-level security. |
| **CORS Configuration** | `@CrossOrigin` or global `WebMvcConfigurer` configuration. |

**What to implement:** Registration → Login (returns JWT) → Protected endpoints (require valid JWT in header) → Role-based access (`ADMIN` vs `USER`).

---

## Phase 5: API Design & REST Best Practices (Week 10)

### 5.1 RESTful API Design Rules

| Rule | Example |
|---|---|
| Use **nouns**, not verbs | ✅ `GET /api/users` ❌ `GET /api/getUsers` |
| Use **plural** nouns | ✅ `/api/users` ❌ `/api/user` |
| Use HTTP methods correctly | `GET` (read), `POST` (create), `PUT` (full update), `PATCH` (partial update), `DELETE` (remove) |
| Use proper status codes | `200 OK`, `201 Created`, `204 No Content`, `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, `409 Conflict`, `422 Unprocessable Entity`, `500 Internal Server Error` |
| Nested resources | `GET /api/users/{userId}/orders` |
| Filtering | `GET /api/users?status=active&age=25` |
| Pagination | `GET /api/users?page=0&size=10&sort=name,asc` |
| Versioning | `GET /api/v1/users` |
| Consistent error format | `{ "error": "NOT_FOUND", "message": "User not found", "timestamp": "..." }` |

### 5.2 API Documentation — Swagger/OpenAPI

Add `springdoc-openapi-starter-webmvc-ui` dependency. Access at `/swagger-ui.html`.

| Annotation | Purpose |
|---|---|
| `@Tag(name = "Users")` | Groups endpoints in Swagger UI |
| `@Operation(summary = "Get user by ID")` | Documents an endpoint |
| `@ApiResponse(responseCode = "200")` | Documents response codes |
| `@Schema(description = "User email")` | Documents DTO fields |

---

## Phase 6: Testing (Weeks 10–11)

> [!WARNING]
> **Untested code is unemployable code.** Companies will specifically ask if you write tests. Having test coverage in your GitHub projects immediately puts you in the top 10% of fresher applicants.

### 6.1 Testing Stack

| Tool | Purpose |
|---|---|
| **JUnit 5** | Test framework. Annotations: `@Test`, `@BeforeEach`, `@AfterEach`, `@BeforeAll`, `@AfterAll`, `@DisplayName`, `@Disabled`, `@ParameterizedTest`, `@Nested`. |
| **Mockito** | Mocking framework. `@Mock`, `@InjectMocks`, `@Spy`. Methods: `when().thenReturn()`, `when().thenThrow()`, `verify()`, `times()`, `never()`, `any()`, `eq()`, `ArgumentCaptor`. |
| **MockMvc** | Test REST controllers without starting the server. `mockMvc.perform(get("/api/users")).andExpect(status().isOk()).andExpect(jsonPath("$.name").value("John"))`. |
| **@SpringBootTest** | Full integration test (loads entire Spring context). |
| **@WebMvcTest(UserController.class)** | Loads only the web layer for a specific controller. |
| **@DataJpaTest** | Loads only JPA components. Uses in-memory H2 database. |
| **Testcontainers** | Spins up real Docker containers (PostgreSQL, Redis, Kafka) for integration tests. **Advanced differentiator.** |
| **AssertJ** | Fluent assertions: `assertThat(result).isNotNull().hasSize(3).contains("John")`. |

### 6.2 Test Structure — AAA Pattern

```java
@Test
@DisplayName("Should return user when valid ID is provided")
void shouldReturnUserWhenValidId() {
    // Arrange
    User user = new User(1L, "John", "john@email.com");
    when(userRepository.findById(1L)).thenReturn(Optional.of(user));

    // Act
    UserResponse result = userService.getUserById(1L);

    // Assert
    assertThat(result).isNotNull();
    assertThat(result.name()).isEqualTo("John");
    verify(userRepository, times(1)).findById(1L);
}
```

---

## Phase 7: Design Patterns You Must Know (Week 11)

> [!NOTE]
> You don't need to memorize all 23 GoF patterns. Know these ones well — they come up in interviews and you'll use them daily in Spring Boot.

| Pattern | Type | Where You'll See It | Example |
|---|---|---|---|
| **Singleton** | Creational | Spring beans are singletons by default | `@Scope("singleton")` |
| **Factory Method** | Creational | Creating objects without specifying exact class | `BeanFactory`, `DriverManager.getConnection()` |
| **Builder** | Creational | Constructing complex objects step by step | Lombok `@Builder`, `StringBuilder`, `UriComponentsBuilder` |
| **Strategy** | Behavioral | Interchangeable algorithms at runtime | Different `PaymentService` implementations injected via DI |
| **Observer** | Behavioral | Event-driven notification | Spring `ApplicationEventPublisher` + `@EventListener` |
| **Template Method** | Behavioral | Define skeleton, let subclasses fill steps | `JdbcTemplate`, `RestTemplate` |
| **Decorator** | Structural | Add behavior without modifying original class | Java I/O Streams, Spring Security filter chain |
| **Proxy** | Structural | Control access to an object | Spring AOP proxies, `@Transactional` proxy |
| **Repository** | Domain-driven | Abstraction over data access | Spring Data `JpaRepository` |
| **DTO** | Architectural | Separate API contract from entity | Request/Response DTOs |
| **Dependency Injection** | Architectural | Core of Spring Framework | Constructor injection |

### 7.1 SOLID Principles (Interview Staple)

| Principle | Meaning | Practical Example |
|---|---|---|
| **S — Single Responsibility** | A class should have only one reason to change | `UserController` handles HTTP. `UserService` handles logic. `UserRepository` handles data. |
| **O — Open/Closed** | Open for extension, closed for modification | Use interfaces. Add new `PaymentStrategy` implementations without changing existing code. |
| **L — Liskov Substitution** | Subtypes must be substitutable for their base types | If `Bird` has `fly()`, don't make `Penguin extends Bird`. Use a `Flyable` interface instead. |
| **I — Interface Segregation** | Don't force clients to depend on interfaces they don't use | Split `AnimalService` into `Swimmable`, `Flyable`, `Walkable` instead of one fat interface. |
| **D — Dependency Inversion** | Depend on abstractions, not concrete implementations | `UserService` depends on `UserRepository` (interface), not `UserRepositoryImpl` (class). |

---

## Phase 8: DevOps Basics — Your Competitive Edge (Week 12)

> [!TIP]
> Most fresher Java developers can only run their app locally using `mvn spring-boot:run`. If you can containerize it, deploy it to AWS, and set up a CI/CD pipeline, you are instantly in the top 5%.

### 8.1 Docker

| Concept | What You Must Know |
|---|---|
| **Dockerfile** | `FROM eclipse-temurin:17-jdk-alpine` → `WORKDIR /app` → `COPY target/*.jar app.jar` → `EXPOSE 8080` → `ENTRYPOINT ["java", "-jar", "app.jar"]` |
| **Multi-stage build** | Stage 1: Maven build. Stage 2: Copy JAR into minimal JDK image. Reduces image size. |
| **Docker Compose** | Define multi-container apps. Your `docker-compose.yml` should run: your Spring Boot app + PostgreSQL + Redis (if used). |
| **Key commands** | `docker build -t myapp .`, `docker run -p 8080:8080 myapp`, `docker-compose up -d`, `docker ps`, `docker logs`, `docker exec -it <id> bash`. |
| **Volumes** | Persist data: `volumes: - postgres_data:/var/lib/postgresql/data`. |
| **Networks** | Containers communicate via service names within the same Docker Compose network. |
| **Environment variables** | Pass config via `-e DB_PASSWORD=secret` or `environment:` in `docker-compose.yml`. **Never hardcode secrets.** |

### 8.2 AWS (What a Fresher Actually Needs)

| Service | What It Does | When You'd Use It |
|---|---|---|
| **EC2** | Virtual machine. | Deploy your Dockerized app. |
| **RDS** | Managed PostgreSQL/MySQL. | Production database. |
| **S3** | Object storage. | Store files, images, backups. |
| **ECR** | Container image registry. | Push your Docker images. |
| **ECS / Fargate** | Container orchestration. | Run Docker containers without managing EC2. |
| **IAM** | Identity & Access Management. | Control who/what can access AWS resources. |
| **CloudWatch** | Logging & monitoring. | View application logs. |
| **Route 53** | DNS. | Map domain name to your app. |
| **SQS** | Message queue. | Async communication between services. |

### 8.3 CI/CD with GitHub Actions

```yaml
# .github/workflows/ci.yml
name: CI/CD Pipeline
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up JDK 17
        uses: actions/setup-java@v4
        with:
          java-version: '17'
          distribution: 'temurin'
      - name: Build and Test
        run: mvn clean verify
      - name: Build Docker Image
        run: docker build -t myapp:latest .
```

---

## Phase 9: Intermediate/Advanced Topics — The Differentiators (Weeks 13–16)

### 9.1 Caching with Redis

| Concept | What You Must Know |
|---|---|
| **Why cache** | Reduce database load, speed up repeated queries. |
| **Spring Cache Abstraction** | `@EnableCaching`, `@Cacheable("users")`, `@CacheEvict("users")`, `@CachePut("users")`. |
| **Redis** | In-memory key-value store. Add `spring-boot-starter-data-redis`. Configure in `application.yml`. |
| **Cache patterns** | Cache-Aside (most common), Write-Through, Write-Behind. |
| **TTL (Time to Live)** | Set expiration on cached data to prevent stale reads. |

### 9.2 Message Queues (Asynchronous Communication)

| Tool | When to Use |
|---|---|
| **RabbitMQ** | Simple task queues, pub/sub, routing. Easier to learn. Good for most use cases. |
| **Apache Kafka** | High-throughput event streaming, log aggregation. Used in FinTech, large-scale systems. |

**Know the pattern:** Producer → Message Broker → Consumer. Decouples services. Enables retry, dead-letter queues, and eventual consistency.

### 9.3 Microservices Concepts (Know the Theory)

| Concept | What You Must Know |
|---|---|
| **Monolith vs Microservices** | Monolith = single deployable unit. Microservices = independently deployable services communicating via APIs/messages. |
| **API Gateway** | Single entry point for all clients. Handles routing, rate limiting, authentication. (Spring Cloud Gateway, Kong) |
| **Service Discovery** | Services register themselves and find each other dynamically. (Eureka, Consul) |
| **Circuit Breaker** | Prevents cascading failures. If a downstream service is down, fail fast instead of waiting. (Resilience4j) |
| **Saga Pattern** | Manage distributed transactions across services using compensating actions. |
| **CQRS** | Command Query Responsibility Segregation — separate read and write models. |
| **Event Sourcing** | Store state changes as a sequence of events rather than current state. |

> [!IMPORTANT]
> **For freshers:** You do NOT need to build a full microservices system. Build a monolith with clean separation (controller → service → repository), understand the microservices concepts theoretically, and be able to discuss trade-offs in interviews. That is sufficient.

### 9.4 Logging & Monitoring

| Tool | Purpose |
|---|---|
| **SLF4J + Logback** | Standard logging in Spring Boot. `LoggerFactory.getLogger(MyClass.class)`. Log levels: `TRACE`, `DEBUG`, `INFO`, `WARN`, `ERROR`. |
| **Structured Logging** | Log in JSON format for machine parsing. Use MDC (Mapped Diagnostic Context) for request tracing. |
| **Spring Actuator** | `/actuator/health`, `/actuator/info`, `/actuator/metrics`, `/actuator/env`. Production-readiness features. |
| **Prometheus + Grafana** | Metrics collection + visualization dashboards. **Bonus differentiator.** |

### 9.5 Database Migrations with Flyway

| Concept | What You Must Know |
|---|---|
| **Why migrations** | Version-control your database schema. Never use `ddl-auto: update` in production. |
| **Naming** | `V1__create_users_table.sql`, `V2__add_email_column.sql`. Versioned and immutable. |
| **Location** | `src/main/resources/db/migration/` |
| **How it works** | Flyway tracks which migrations have been applied in a `flyway_schema_history` table. On startup, it runs any new migrations automatically. |

---

## Phase 10: DSA for Interviews (Ongoing — Throughout All Phases)

> [!CAUTION]
> You WILL face an online coding round in 80%+ of fresher interviews in India. If you can't solve Easy/Medium LeetCode problems in 20–30 minutes, you'll be eliminated before anyone even looks at your Spring Boot projects.

### Target: 150 Problems in Java

| Topic | Must-Know Patterns | LeetCode Count |
|---|---|---|
| **Arrays & Strings** | Two pointers, sliding window, prefix sum, kadane's algorithm | 30 problems |
| **HashMap & HashSet** | Frequency counting, two-sum pattern, grouping, anagram detection | 15 problems |
| **Sorting & Searching** | Binary search (on sorted arrays AND on answer space), merge sort | 15 problems |
| **Stack & Queue** | Monotonic stack, next greater element, valid parentheses, BFS using queue | 15 problems |
| **Linked List** | Fast/slow pointers (cycle detection), reverse, merge two sorted lists | 10 problems |
| **Trees & BST** | DFS (inorder/preorder/postorder), BFS (level order), height, diameter, validate BST, LCA | 20 problems |
| **Graphs** | BFS, DFS, connected components, topological sort, detect cycle | 15 problems |
| **Dynamic Programming** | Fibonacci, climbing stairs, coin change, longest common subsequence, 0/1 knapsack | 15 problems |
| **Greedy** | Activity selection, interval scheduling, jump game | 10 problems |
| **Recursion/Backtracking** | Subsets, permutations, N-Queens, Sudoku solver | 5 problems |

### Time Complexity Cheat Sheet

| Complexity | Name | Example |
|---|---|---|
| O(1) | Constant | HashMap get/put, array access by index |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Single loop, linear search |
| O(n log n) | Linearithmic | Merge sort, heap sort, `Arrays.sort()` |
| O(n²) | Quadratic | Nested loops, bubble sort |
| O(2ⁿ) | Exponential | Recursive fibonacci (without memo), subsets |
| O(n!) | Factorial | Permutations |

---

## Phase 11: CS Fundamentals for Interviews (Week 14)

### 11.1 Operating Systems

| Topic | Key Points |
|---|---|
| **Process vs Thread** | Process = independent, own memory space. Thread = lightweight, shares process memory. |
| **Multithreading** | Concurrency vs parallelism. Context switching overhead. |
| **Process Scheduling** | FCFS, SJF, Round Robin, Priority Scheduling. |
| **Deadlock** | Conditions: Mutual exclusion, hold and wait, no preemption, circular wait. Prevention strategies. |
| **Memory Management** | Paging, segmentation, virtual memory, page replacement (LRU, FIFO). |
| **File System** | Inodes, file descriptors, permissions (`chmod`, `chown`). |

### 11.2 Computer Networks

| Topic | Key Points |
|---|---|
| **OSI / TCP-IP Model** | 7 layers (OSI) vs 4 layers (TCP/IP). Know which protocols operate at which layer. |
| **TCP vs UDP** | TCP = reliable, ordered, connection-oriented (HTTP, SSH). UDP = fast, unreliable (DNS, video streaming). |
| **HTTP/HTTPS** | Request/Response cycle. Methods (GET, POST, PUT, DELETE). Status codes. Headers. HTTPS = HTTP + TLS encryption. |
| **DNS** | Resolves domain names to IP addresses. DNS lookup chain: Browser cache → OS cache → Router → ISP → Root DNS. |
| **REST vs GraphQL vs gRPC** | REST = resource-based, stateless. GraphQL = query language, client asks for exact data. gRPC = binary protocol, fast, used in microservices. |
| **WebSockets** | Full-duplex communication (chat apps, real-time feeds). |
| **Load Balancer** | Distributes traffic across servers. Algorithms: round-robin, least connections, IP hash. |
| **CDN** | Content Delivery Network. Serves static assets from geographically close servers. |

### 11.3 Linux Commands (Used Daily in Backend Work)

```bash
# Navigation & Files
ls -la, cd, pwd, mkdir -p, rm -rf, cp, mv, cat, head, tail, less, find, locate

# Text Processing
grep -r "pattern" ., grep -i, grep -n, awk, sed, cut, sort, uniq, wc -l

# Process Management
ps aux, top, htop, kill -9 <PID>, nohup, &, jobs, fg, bg

# Networking
curl -X GET/POST, wget, ping, netstat -tlnp, ss -tlnp, nslookup, dig, traceroute

# Disk & Memory
df -h, du -sh, free -m

# Permissions
chmod 755, chmod +x, chown user:group, sudo

# Package Management
apt update, apt install, yum install

# System
systemctl start/stop/status, journalctl -u service, env, export, source

# SSH
ssh user@host, ssh-keygen, scp file user@host:/path, ssh-copy-id
```

---

## Phase 12: The Two Projects That Get You Hired (Weeks 12–16)

> [!IMPORTANT]
> These projects must be **on GitHub** with a clean README, proper commits, and working code. A recruiter or interviewer WILL check your GitHub.

### Project 1: Wallet/Banking System (Monolith with All Best Practices)

**Features:**
- User registration & login (JWT authentication)
- Wallet creation, credit, debit, transfer between wallets
- Transaction history with pagination & filtering
- Role-based access (USER vs ADMIN)
- Input validation on all endpoints
- Global exception handling
- Database migrations with Flyway
- Unit tests (Service layer with Mockito) + Integration tests (Controller with MockMvc)
- API documentation with Swagger/OpenAPI

**Tech Stack:** Java 17, Spring Boot 3, Spring Security + JWT, Spring Data JPA, PostgreSQL, Flyway, MapStruct, Docker, Docker Compose.

**What this proves:** You can build a complete, production-quality backend application with authentication, proper layered architecture, and testing.

---

### Project 2: Same Project — But Cloud-Deployed with CI/CD

Take Project 1 and add:
- Multi-stage Dockerfile (build + runtime)
- Docker Compose (app + PostgreSQL + Redis)
- Redis caching on frequently-read endpoints (`@Cacheable`)
- GitHub Actions CI/CD pipeline (build → test → Docker build → push to ECR → deploy to EC2/ECS)
- Basic monitoring with Spring Actuator
- Architecture diagram in README

**What this proves:** You are not just a code writer. You understand how to ship software to production.

---

### README Template for Projects

```markdown
# 🏦 Wallet Service

A production-grade digital wallet backend built with Java 17 and Spring Boot 3.

## Tech Stack
Java 17 | Spring Boot 3 | PostgreSQL | Redis | Docker | AWS | GitHub Actions

## Architecture
[Include a simple diagram — even a text-based one]

Controller → Service → Repository → PostgreSQL
                ↕
              Redis Cache

## Features
- [x] JWT Authentication & Authorization
- [x] Wallet CRUD + Transfer operations
- [x] Transaction history with pagination
- [x] Input validation & global error handling
- [x] Redis caching
- [x] Database migrations (Flyway)
- [x] 85%+ test coverage
- [x] Dockerized deployment
- [x] CI/CD with GitHub Actions

## API Endpoints
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | /api/v1/auth/register | Register user | No |
| POST | /api/v1/auth/login | Login (returns JWT) | No |
| GET | /api/v1/wallets/{id} | Get wallet | USER |
| POST | /api/v1/wallets/{id}/transfer | Transfer funds | USER |
| GET | /api/v1/admin/users | List all users | ADMIN |

## How to Run
```bash
docker-compose up -d
```

## How to Test
```bash
mvn clean verify
```
```

---

## The Complete Technology Summary

| Layer | Technology |
|---|---|
| **Language** | Java 17+ |
| **Framework** | Spring Boot 3.x |
| **ORM** | Spring Data JPA + Hibernate |
| **Database** | PostgreSQL |
| **Caching** | Redis |
| **Security** | Spring Security + JWT |
| **Validation** | Jakarta Validation |
| **Migrations** | Flyway |
| **Mapping** | MapStruct |
| **API Docs** | SpringDoc OpenAPI (Swagger) |
| **Testing** | JUnit 5, Mockito, MockMvc, AssertJ, Testcontainers |
| **Build Tool** | Maven |
| **Containerization** | Docker, Docker Compose |
| **CI/CD** | GitHub Actions |
| **Cloud** | AWS (EC2, RDS, S3, ECR, ECS) |
| **Monitoring** | Spring Actuator, SLF4J + Logback |
| **Version Control** | Git + GitHub |
| **IDE** | IntelliJ IDEA (Community Edition is free) |
| **API Testing** | Postman or Bruno |

---

## Weekly Schedule (6-Month Plan)

| Week | Focus | Deliverable |
|---|---|---|
| 1–2 | Core Java: OOP, Collections, Exception Handling | Solve 30 basic Java problems |
| 3–4 | Core Java: Streams, Generics, Multithreading, Java 8+ | Complete Core Java notes |
| 5 | Maven, Git, Project Structure, SQL basics | Set up first Spring Boot project skeleton |
| 5–6 | SQL deep dive: JOINs, subqueries, indexing, schema design | Design 3 database schemas |
| 6–8 | Spring Boot: REST APIs, JPA, Validation, Exception Handling | Build basic CRUD API |
| 9–10 | Spring Security + JWT, DTO pattern, MapStruct, Swagger | Add auth to your CRUD API |
| 10–11 | Testing: JUnit 5, Mockito, MockMvc, Integration Tests | Achieve 80%+ test coverage on your project |
| 11 | Design Patterns, SOLID Principles | Refactor your project using patterns |
| 12 | Docker, Docker Compose, Flyway | Dockerize your app + PostgreSQL |
| 12–16 | **Build Project 1 (Wallet System)** | Complete, tested, documented on GitHub |
| 13–16 | Redis caching, GitHub Actions CI/CD, AWS deployment | **Project 2 (Cloud-deployed version)** |
| 14 | CS Fundamentals: OS, Networks, Linux | Interview prep notes |
| **Ongoing** | **DSA: 150 LeetCode problems** | **20–25 problems per week** |
| 17–20 | Mock interviews, resume optimization, job applications | Start applying by week 17 |
| 20–24 | Aggressive job hunting: referrals, LinkedIn, Naukri, Wellfound | **Land the job** |

---

> [!TIP]
> **The secret nobody tells you:** The difference between a fresher who gets hired at ₹4 LPA (service company) and one who gets hired at ₹10+ LPA (product company) is not intelligence. It's **the two projects on GitHub + the ability to solve LeetCode mediums + clear communication in interviews.** That's it. No magic. No shortcuts. Just focused, consistent effort for 6 months.
