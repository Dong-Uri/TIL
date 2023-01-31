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
