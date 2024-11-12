const { useState, useEffect, useLayoutEffect, useMemo } = React;
// import { getTree, getSpeak, getLesson } from "/static/services/lesson.service.js";

const root = ReactDOM.createRoot(document.getElementById("folder-tree"));

const convert_string_to_bool = (data) =>
  typeof data === "boolean" ? data : JSON.parse(data?.toLowerCase() || "false");

const Loadding = () => {
  return (
    <div className="text-center">
      <h1>ĐANG TẢI...</h1>
    </div>
  );
};

function App() {
  const [treeData, setTreeData] = useState({});
  const [speakLink, setSpeakLink] = useState({});
  const [lessonData, setLessonData] = useState({});

  const [loaddingTree, setLoaddingTree] = useState(false);
  const [loaddingSpeak, setLoaddingSpeak] = useState(false);
  const [loaddingLesson, setLoaddingLesson] = useState(false);

  const urlGetQuery = useMemo(
    () =>
      Object.fromEntries(new URLSearchParams(window.location.search).entries()),
    [window, lessonData]
  );
  const urlNavigate = ({ path = "/", params = {} }) => {
    var url = new URL(
      // path,
      window.location
    );
    Object.keys(params).map((param) =>
      url.searchParams.set(param, params[param])
    );
    window.history.pushState({}, "", url);
  };

  const subjectSlug = useMemo(() => urlGetQuery.subject);

  const fetchTree = () => {
    setLoaddingTree(true);
    const { subject, chapter, lesson } = urlGetQuery;

    getTree(subject, chapter, lesson)
      .then((response) => {
        const data = response?.data;
        setTreeData(data);
        setLoaddingTree(false);
      })
      .catch((error) => {});
  };
  const fetchSpeak = (lesson) => {
    setLoaddingSpeak(true);

    getSpeak(lesson)
      .then((response) => {
        setSpeakLink(response?.data);
      })
      .catch((error) => {})
      .finally(() => setLoaddingSpeak(false));
  };
  const fetchLesson = (lesson) => {
    setLoaddingLesson(true);

    getLesson(lesson)
      .then((response) => {
        setLessonData(response?.data);
        setSpeakLink({});
        setLoaddingLesson(false);
      })
      .catch((error) => {});
  };

  const handleGetSpeak = (e) => {
    const { lesson } = urlGetQuery;
    fetchSpeak(lesson);
  };
  const handleGetLesson = (chapter, lesson) => {
    urlNavigate({
      params: {
        subject: subjectSlug,
        chapter,
        lesson,
        limit: 5,
        page: 1,
      },
    });

    fetchLesson(lesson);
  };

  useLayoutEffect(() => {
    fetchTree();
  }, []);

  useEffect(() => {
    const { lesson } = urlGetQuery;
    fetchLesson(lesson);
  }, []);

  useEffect(() => {
    $(document).ready(function () {
      $(this)
        .find("div[data-lesson]")
        .each(function () {
          const { lesson } = urlGetQuery;
          const chapter = $(this).data("chapter");
          const lessonData = $(this).data("lesson");

          if (lesson == lessonData) {
            $(this).addClass("text-danger");
            // handleGetLesson(chapter, lesson);
          }
        });

      $("div.tree-title").click(function () {
        $(this)
          .parent()
          .has("ul.tree-root")
          .children("ul.tree-root")
          .toggle(function () {
            if ($(this).css("display") == "none") {
              //change the button label to be 'Show'
              //toggle_switch.html('Show');
            } else {
              //change the button label to be 'Hide'
              //toggle_switch.html('Hide');
            }
            return 300;
          });
      });
      $(".tree-node:not(.root) > div[data-lesson]").click(function () {
        $("div[data-lesson]").removeClass("text-danger");
        const chapter = $(this).data("chapter");
        const lesson = $(this).data("lesson");
        $(this).addClass("text-danger");
        if (lesson) {
          handleGetLesson(chapter, lesson);
        }
      });
    });
  }, [treeData]);

  const generateTree = (data = {}) => {
    return (
      <ul
        className={`tree-root`}
        style={{
          display:
            convert_string_to_bool(data?.isRoot) ||
            convert_string_to_bool(data?.isExpand)
              ? "block"
              : "none",
        }}
      >
        {data?.children?.map((element, indexChapter) => (
          <li
            className={`tree-node ${
              convert_string_to_bool(data?.isRoot) ? "root" : "child"
            }`}
            key={indexChapter}
          >
            <div
              data-chapter={data?.slug}
              data-lesson={element?.slug}
              className="tree-title"
            >
              <span className="tree__title-number">{element.order}</span>
              <span className="tree__title-content">{element.title}</span>
            </div>
            {element?.children && generateTree(element)}
          </li>
        ))}
      </ul>
    );
  };
  const generateSpeak = () => {
    return (
      <>
        {loaddingSpeak ? (
          <Loadding />
        ) : (
          <>
            {/* lessonData?.audio_file ? ( */}
            {speakLink?.mp3 ? (
              <audio style={{ width: "100%" }} controls>
                <source src={speakLink?.mp3} type="audio/mpeg" />
                {/* <source
                  src="https://www.w3schools.com/html/horse.ogg"
                  type="audio/ogg"
                />
                <source
                  src="https://www.w3schools.com/html/horse.wav"
                  type="audio/wav"
                /> */}
                Your browser does not support the audio element.
              </audio>
            ) : (
              <button
                className="button rounded-0 primary-bg w-100 btn_1 genric-btn m-3"
                onClick={handleGetSpeak}
              >
                Nghe bài
              </button>
            )}
          </>
        )}
      </>
    );
  };

  return (
    <>
      <div>
        <h2>Chi tiết</h2>
        <ul className="blog-info-link mt-3 mb-4">
          <li>
            <a href="#">
              <i className="fa fa-user" />
              10 Lượt xem
            </a>
          </li>
          <li>
            <a href="#">
              <i className="fa fa-comments" /> 03 Comments
            </a>
          </li>
          <li>
            <a href="#">
              <i className="fa fa-calendar" />
              Ngày tạo: {lessonData?.created}
            </a>
          </li>
        </ul>
      </div>
      {/*  */}
      <div className="row">{generateSpeak()}</div>
      {/*  */}
      <div className="row">
        <div className="col-md-4">
          <div className="border-right border-secondary rounded px-2 py-1">
            {loaddingTree ? <Loadding /> : generateTree(treeData)}
          </div>
        </div>
        <div className="col-md-8">
          <div className="row">
            {loaddingLesson ? (
              <Loadding />
            ) : (
              <div
                dangerouslySetInnerHTML={{
                  __html: DOMPurify.sanitize(lessonData?.content),
                }}
              ></div>
            )}
          </div>
        </div>
      </div>
      {/* CAPTION */}
      <div className="quote-wrapper">
        <div className="quotes">{lessonData?.caption}</div>
      </div>
    </>
  );
}

root.render(<App />);
