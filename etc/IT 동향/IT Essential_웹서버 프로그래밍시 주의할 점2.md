## 캐시

> 데이터를 임시로 저장해두는 장소
>
> 사용자가 요청한 웹 페이지를 캐시에 저장 후 같은 페이지로 재 요청 시 캐시에서 제공하여 시간과 네트워크 통신, DB 부하를 줄일 수 있다.

### EHCache [(EHCache)](https://www.ehcache.org/)

* JAVA기반 오픈 소스 기반의 Local Cache
* 속도가 빠르고 경량 Cache라는 장점이 있음.
* 서버 간 분산 캐시를 지원

### Redis [(Remote Dictionary Server)](https://redis.io/)

* 오픈소스 비관계형 기반의 DBMS
* key-value 구조를 가진 In-mamory data structure
* 다양한 데이터 구조를 제공 (string, set, sorted set, hash 등 )

### [**비교 사이트 - DB-engines**](https://db-engines.com/en/system/Ehcache%3bMemcached%3bRedis)



## logging

### spring Boot

1. [Logback](http://logback.qos.ch/manual/index.html)

   * JAVA 오픈소스 logging framework 
   * slf4j 지원 (연관 라이브러리들이 다른 logging framework를 쓰더라도 logback으로 통합할 수 있도록 함.)
   * spring Boot의 기본으로 설정되어 있음.
   * 가장 성능이 우수하여 최근에 많이 사용되고 있음. (log4j보다 약 10배 정도 빠르게 수행)
   * 5가지 로그 메세지 레벨을 사용 (TRACE, DEBUG, INFO, WARN, ERROR)
   * [설정 방법 참고](https://goddaehee.tistory.com/206)

2. Log4j

   * JAVA 오픈소스 라이브러리

   * 효율적인 메모리 관리로 과거에 많이 사용.
   * 계층적인 로그 설정과 처리를 지원. 
   * 6가지 로그 메세지 레벨을 사용 (TRACE, DEBUG, INFO, WARN, ERROR, FATAL)
   * 속도에 최적화 되어 있음.
   * 최근 [Log4j 2 출시](https://logging.apache.org/log4j/2.x/)
   * [설정 방법 참고](https://twofootdog.tistory.com/52)

3. Java Util Logging

   * JAVA에서 제공하는 기본 Log

### django

1. django logging
   * Python에 내장된 로깅 시스템 사용
   * [설정 방법 참고](https://docs.djangoproject.com/ko/3.0/topics/logging/#configuring-logging)

### NodeJS

1. [winston](https://www.npmjs.com/package/winston)

   * Node.js에서 가장 많이 쓰이는 라이브러리
   * 설정 파일을 구성하여 사용자가 직접 로그를 남기는 것이 가능

   * [설정 방법 참고](https://velog.io/@ash/Node.js-%EC%84%9C%EB%B2%84%EC%97%90-logging-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC-winston-%EC%A0%81%EC%9A%A9%ED%95%98%EA%B8%B0)

2. [morgan](https://github.com/expressjs/morgan)

   * express.js에서 기본으로 제공하는 미들웨어
   * HTTP메서드로 특정 URL을 방문할 때 함수가 호출

