(정리 도움받음)

#1

JPA
ORM(Object-Relational Mapping) 프레임워크
.java만으로 쿼리 없이 DB 정의, 테이블 매핑, DB 사용 등이 가능하게 하는 라이브러리가 JPA다
JPA를 구현한 대표적인 오픈소스로는 Hibernate가 있다
쿼리를 몰라도 사용할 수 있고, 러닝 커브가 낮다
Table명이 되는 @Entity, 쿼리가 되는 JpaRepository만 작성하면 사용할 수 있다

@Entity
public class table_name {
// 릴레이션 정의
}

릴레이션 정의 시에는 다중성, 방향성, 연관관계의 주인을 고려해야 한다
1:1 @OneToOne 1:N @OneToMany N:1 @ManyToOne N;M @ManyToMany
양방향은 실무에서 위험성 때문에 잘 쓰지 않는다 양방향도 결국은 단방향의 쌍이다
엔티티를 양방향 연관관계로 설정하면 객체의 참조는 둘인데 외래 키는 하나라서 양방향을 사용할 경우 연관관계의 주인을 설정해야 한다
연관관계의 주인: 두 객체 연관관계 중 하나를 정해서 테이블의 외래키를 관리 주인 외에는 READ만 가능하다 (Freign key를 소유하고 있는 쪽이 주인)

Read : find로 시작
Delete: delete로 시작
Create: save
Update: 객체 조회 후 값 변경 후 save

객체 생성 시에는 Lombok의 @Burilder를 쓰면 좋다. 직접 내용을 입력하면 실수할 경우 타격이 크다. 따라서 @Burilder를 이용해서 매핑하는 편이 좋다.
AUTOINCREMENT로 하면 양수만 사용하는데 범위를 키우고 싶다면 INT UNSIGNED 사용한다
db 보안과 민감 정보 보호를 위해서 entity 값 그대로 주면 안되고 새로운 객체에 담아서 반환한다
CORS는 BACK에서 해결 (Spring Security)

https://docs.spring.io/spring-data/jpa/docs/current/reference/html/https://spring.io/projects/spring-data-jpahttps://arahansa.github.io/docs_spring/jpa.html

#2

Spring Boot JPA
Learning Goals
SpringBoot JPA가 무엇인지 알 수 있다.
SpringBoot JPA로 DB모델 설계를 할 수 있다.
SpringBoot JPA로 CRUD를 할 수 있다.
Object-Relational Mapping
객체 관계 매핑
위키백과, 우리 모두의 백과사전
객체 관계 매핑(Object-relational mapping: ORM)은 데이터베이스와 객체 지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기 법이다. 객체 지향 언어에서 사용할 수 있는 가상 객체 데이터베이스를 구축하는 방법이다. 객체 관계 매핑을 가능하게 하는 상용 또는 무료 소프트웨 어 패키지들이 있고, 경우에 따라서는 독자적으로 개발하기도한다.
Javax.persistence, JPA API, Entity Manager Factory, Entity Transaction, Entity, Entity Manager, Query, Persistence

@Entity
JpaRepository

꿀팁: 키값을 오토인크리먼트로 하면 키값 -1인경우가 있을까없을까 - 없다

unsigned로 하는것이 꿀팁

spring.datasource.url=jdbc: h2:mem:testdb

spring.jpa.generate-ddl=true 
spring.jpa.hibernate.ddl-auto=create

spring.jpa.show-sql=true
spring.jpa.properties.hibernate.format_sql=true
logging.level.org.hibernate.type.descriptor.sql.BasicBinder=trace
프로퍼티 설정
application.properties 또는 application.yml

spring.jpa.generate-ddl=true
spring.jpa.hibernate.ddl-auto-update

spring.jpa.show-sql=true
spring.jpa.properties.hibernate.format_sql=true
logging.level.org.hibernate.type.descriptor.sql.BasicBinder=trace
import lombok.ToString;

@Entity
@NoArgsConstructor
@Getter
@Setter
@ToString
public class Board {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(columnDefinition = "INT UNSIGNED")
    private int uid;

    @OneToMany (mapped By "boardUid")
    private List<Reply> reply = new ArrayList<>();
    private String user;
    private LocalDateTime createdDate;
    private String ip;
    private String title;
    private String contents;
    private int how;
    
    @Builder
    public Board(String user, LocalDateTime createDate, String ip, String title, ....
        this.user = user;
        this.createDate = createDate;
Relationship Mapping
단방향?양방향?

조회테이블? 참조테이블?

@OneToOne
@OneToMany
@ManyToOne
@JoinColumn
일대일? 일대다? 다대일? 다대다?

대중성
일대일(1:1) @OneToOne
일대다(1:N) @OneToMany
다대일(N:1) @ Many ToOne
다대다(N:M) @Many ToMany
일대다 != 다대일 1:N != N:1
게시물을 조회 하고 댓글을 가져올 것인가? 댓글을 조회 하고 그것이 어떤 게시글을 가져올 것인가? →비즈니스 로직에 따라 다르다!

방향성
@JoinColumn

Object A → Object B

Object B → Object A

Object A ↔ Object B

이런 양방향은 JPA에서는 지양해주세요!

연관 관계의 주인
@OneToMany(mappedBy="boardFk") 

// @JoinColumn(name="boardFk")
양방향일경우 어떤 테이블 기준으로
데이터를 삭제 하면 그것에 관련된 데이터들을 다 삭제 할 것인가?
→FK 키 관리 주인을 설정해 준다.
→→ '다' 쪽이 주인이다.
→→→ @Many ToOne 은 항상 주인이다.

@GetMapping("/{uid}")
    public Map<String, Object> board (@PathVariable int uid)
    var option = boardRepository.findById(uid);
    if (!option.isPresent()) return null;
    Board board = option.get();
    Map<String, Object> obj = new HashMap<>();
    obj.put("uid", board.getUid());
    obj.put("title", board.getTitle()); obj.put("contents", board.getContents()); obj.put("reply", board.getReply());
    return obj;
}
@DeleteMapping("/{uid}")
    public void delete (@PathVariable int uid) { boardRepository.deleteById(uid);
}
@PostMapping
public int post (@RequestBody Map<String, Object> body) { 
    return boardRepository.save(Board.builder()
    .user(body.get("user").toString())
    .title(body.get("title").toString())
    .contents(body.get("contents").toString())
    .createdDate(LocalDateTime.now())
    .build()).getUid();
}
@Builder
@Builder
public Board(String user, LocalDateTime createdDate, String ip, String title, String contents, int how) {
    this.user user;
    this.createdDate createdDate;
    this.ip-ip;
    this.title title;
    this.contents = contents;
    this.how how;
}

new Board("user", LocalDateTime.now(), "123.123.123.123", "title", "contents",1);
return boardRepository.save(Board.builder()
    .user(body.get("user").toString())
    .title(body.get("title").toString())
    .contents(body.get("contents").toString())
    .createdDate(LocalDateTime.now())
    .build()).getUid();
SpringBoot JPA Docs
public interface Board Repository extends JpaRepository<Board, Integer> {
public List<Board> findTop1000ByOrderByUidDesc();
}
Supported keywords inside method names
스프링부트 JPA docs
https://docs.spring.io/spring-data/jpa/docs/current/reference/html/#jpa.query-methods.query-creation

Summary & Quiz
SpringBoot JPA는 (**)라는 ORM 프레임워크를 사용해서 구현한다.
Hibernate
     

기본적으로 제공되는 레파짓토리 메소드이름 중에 조회에 사용되는 메소드는 (****)로 시작되는 메소드이다.
find
     

JPA를 사용할 때 꼭 구현해 줘야 하는 두가지는 (★★★)와 레파짓토리 이다.
Entity(엔티티)
   

연관관계를 설정할 때에는 3가지를 설정해 주어야 하는데 다중성, (***), 연관관계 주인을 설정해 주어야 한다.
방향성(단방향, 양방향) 

