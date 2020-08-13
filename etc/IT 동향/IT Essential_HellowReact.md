[TOC]

# React Lifecycle

## class형 component

### mount

1. [constructor()](https://ko.reactjs.org/docs/react-component.html#constructor)

   > component 생성자.
   >
   > 해당 컴포넌트가 마운트되기 전에 호출된다.
   >
   > 메스드를 바인딩하거나 state를 초기화할 때 사용.

2. [static getDerivedStateFromProps()](https://ko.reactjs.org/docs/react-component.html#static-getderivedstatefromprops)

   > render() 를 호출하기 직전에 호출.
   >
   > 시간이 흐름에 따라 변하는 props에 state가 의존하는 경우에 사용.

3. [render()](https://ko.reactjs.org/docs/react-component.html#render)

   > **클래스 컴포넌트에서 반드시 구현해야하는 유일한 메서드**
   >
   > props와 state 값을 활용하여 페이지를 그림.

4. [componentDidMount()](https://ko.reactjs.org/docs/react-component.html#componentdidmount)

   > 컴포넌트가 마운트된 직후에 호출.
   >
   > 외부에서 데이터를 불러오거나 DOM 노드가 필요한 초기화 작업을 수행.



### update

1. static getDerivedStateFromProps()

2. [shouldComponentUpdate()](https://ko.reactjs.org/docs/react-component.html#shouldcomponentupdate)

   > props 또는 state가 새로운 값으로 갱신되어서 렌더링이 발생하기 직전에 호출.
   >
   > props 또는 state의 변화로 인해 컴포넌트의 출력 결과에 영향이 미치는지를 react가 알 수 있도록 함.

3. render()

4. [getSnapshotBeforeUpdate()](https://ko.reactjs.org/docs/react-component.html#getsnapshotbeforeupdate)

   > 가장 마지막으로 렌더링된 결과가 DOM 등에 반영되었을 때 호출.
   >
   > 새로운 값으로 변경되기 전에 이전 값들을 얻어 componentDidUpdate()에 인자로 전달
   >
   > -> ex) 스크롤 위치 등을 파악 하여 새로 렌더링 되더라도 같은 위치를 보여 줌.

5. [componentDidUpdate()](https://ko.reactjs.org/docs/react-component.html#componentdidupdate)

   > 값의 갱신이 일어난 직후에 호출.
   >
   > 필요에 따라 api요청을 다시 보낸다던가 하는 작업을 수행.

   

### unmount

1. [componentWillUnmount()](https://ko.reactjs.org/docs/react-component.html#componentwillunmount)

   > 컴포넌트가 마운트 해제되어 제거되기 직전에 호출.



# 여기서 잠깐!

**저희 스켈레톤 코드는 class로 작성이 안되어있는데 어떻게 적용하나요??**

[react 공식 답변](https://ko.reactjs.org/docs/hooks-faq.html#how-do-lifecycle-methods-correspond-to-hooks)

## function형 component

### Hook [(HooK)](https://ko.reactjs.org/docs/hooks-intro.html)

> 함수 컴포넌트에서 React state와 생명주기 기능을 연동할 수 있게 해주는 함수.
>
> class없이 react를 사용할 수 있게 해준다.

1. State Hook [(useState)](https://ko.reactjs.org/docs/hooks-state.html)

   > 현재 state 값과 이 값을 업데이트하는 함수를 쌍으로 제공.
   >
   > 상태값을 관리하기 위해 사용.
   >
   > ex. const [count, setCount] = useState(초기값);

2. Effect Hook [(useEffect)](https://ko.reactjs.org/docs/hooks-effect.html)

   > componentDidMount, componentDidUpdate, componentWillUnmount를 하나로 통합한 기능을 제공.
   >
   > 매 렌더링 이후에 useEffect()를 호출. 
   >
   > 선택적으로 사용하면 안된다. (조건문 안에서 사용)

3. Context Hook [(useContext)](https://ko.reactjs.org/docs/hooks-reference.html#usecontext)

   > context 객체를 받아 그 context의 현재 값을 반환.
   >
   > props를 넘기는 과정의 효율성을 높이기 위해 사용.

4. [추가 제공 hooks](https://ko.reactjs.org/docs/hooks-reference.html#additional-hooks)

   * useReducer
   * useCallback
   * useMemo
   * useRef
   * useImperativeHandle
   * useLayoutEffect
   * useDebugValue



# Redux

자바스크립트 애플리케이션에서 흔히 쓰이는 상태 컨테이너.

**사용하는 이유**

1. 계속해서 바뀌는 많은 데이터들이 있을 때.
2. 상태값을 위한 믿을만한 하나의 장소가 필요할 때.
3. 모든 상태값을 가지고 있기에는 최상위 컴포넌트가 더 이상 적당하지 않을 때.

**3가지 원칙**

1. Single source of truth

   > store에서 모든 데이터를 전역적으로 관리.

2.  State is read-only

    > 상태값은 읽기전용이다.
    >
    > 상태값을 변화시키려면 action을 활용해야 한다.

3.  Changes are made with pure functions

    > action에 의해 상태 트리가 어떻게 변화하는지 지정하기 위해 순수 Reducer를 작성해야 한다.



# Q&A

1. Q : 사용량 말고 성능은 어떤 것이 좋나요? 

   A : 성능면에서는 react와 vue 둘다 많이 고도화 되어 있기 때문에 비등비등 하다고 생각합니다. 

2. Q : useState랑 useEffect같은 hook들은 언제 실행되는지 알려주실수 있나요? 

   A : 오늘 방송에서 말씀드린 공식 홈페이지에 잘 나와있습니다. 참고 하실만한 2가지 링크 보내드릴께요. 공식 레퍼런스에는 더 많은 내용들이 있습니다.  

   - https://ko.reactjs.org/docs/hooks-intro.html  
   - https://overreacted.io/ko/a-complete-guide-to-useeffect/