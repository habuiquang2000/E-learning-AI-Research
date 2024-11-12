// https://stackoverflow.com/questions/17293861/how-to-make-input-type-file-accept-only-these-types
const { useState, useEffect, useLayoutEffect, useMemo } = React;

const root = ReactDOM.createRoot(document.getElementById("document-office"));

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
  const [loaddingUpload, setLoaddingUpload] = useState(false);

  const [categories, setCategories] = useState([]);
  const [subjects, setSubjects] = useState([]);
  const [chapters, setChapters] = useState([]);

  const [fields, setFields] = useState({
    category: "",
    subject: "",
    chapter: "",

    title: "",
    order: "",
    caption: "",
    content: "",
  });

  const [selectedFile, setSelectedFile] = useState(null);
  const [messages, setMessages] = useState([]);

  const fetchCategories = () => {
    getCategories()
      .then((response) => {
        const data = response?.data;

        setCategories(data);
      })
      .catch((error) => {
        console.error(error);
      });
  };
  const fetchSubjects = (category) => {
    getSubjects(category)
      .then((response) => {
        const data = response?.data;

        setSubjects(data);

        if (data.length === 0) {
          setChapters(data);
          setFields((prev) => ({
            ...prev,
            subject: "",
            chapter: "",
          }));
        }
      })
      .catch((error) => {
        console.error(error);
      });
  };
  const fetchChapters = (subject) => {
    getChapters(subject)
      .then((response) => {
        const data = response?.data;

        setChapters(data);
      })
      .catch((error) => {
        console.error(error);
      });
  };
  const fetchLessons = (lesson) => {
    // getChapters(lesson)
    //   .then((response) => {
    //     const data = response?.data;
    //     setChapters(data);
    //   })
    //   .catch((error) => {
    //     console.error(error);
    //   });
  };

  const handleFieldChange = (event) => {
    const { value, id } = event.target;

    setFields((prev) => ({
      ...prev,
      [id]: value,
    }));
  };
  const handleCategoryChange = (event) => {
    const { value } = event.target;
    handleFieldChange(event);
    fetchSubjects(value);
  };
  const handleSubjectChange = (event) => {
    const { value } = event.target;
    handleFieldChange(event);
    fetchChapters(value);
  };
  const handleChapterChange = (event) => {
    const { value } = event.target;
    handleFieldChange(event);
    fetchLessons(value);
  };

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
  };
  const handleFileUpload = (event) => {
    const formData = new FormData();
    formData.append("file", selectedFile);
    setLoaddingUpload(true);

    postDocumentFile(formData)
      .then((response) => {
        const data = response?.data;

        setFields((prev) => ({
          ...prev,
          content: data,
        }));
        setLoaddingUpload(false);
        // if (convert_string_to_bool(data)) window.location.href = "/teacher/";
      })
      .catch((error) => {
        console.error(error);
        setLoaddingUpload(false);
      });
  };
  const handleContentUpload = (e) => {
    setLoaddingUpload(true);

    postDocumentContent(fields)
      .then((response) => {
        const data = response?.data;

        setLoaddingUpload(false);
        if (convert_string_to_bool(data)) window.location.href = "/teacher/";
      })
      .catch((error) => {
        console.error(error);
        setLoaddingUpload(false);
      });
  };

  useLayoutEffect(fetchCategories, []);

  return (
    <>
      <div className="module" id="changelist">
        <div className="results">
          <div className="form-group">
            <label htmlFor="category">Danh mục</label>
            <select
              onChange={handleCategoryChange}
              value={fields.category}
              className="form-control"
              id="category"
            >
              <option value="">LỰA CHỌN</option>
              {categories.map((category, index) => (
                <option key={index} value={category.slug}>
                  {category.title} ({category.childrenCount} Bài)
                </option>
              ))}
            </select>
          </div>

          <div className="row">
            <div className="col">
              <div className="form-group">
                <label htmlFor="subject">Môn học</label>
                <select
                  disabled={fields.category == ""}
                  onChange={handleSubjectChange}
                  value={fields.subject}
                  className="form-control"
                  id="subject"
                >
                  <option value="">LỰA CHỌN</option>
                  {subjects.map((subject, index) => (
                    <option key={index} value={subject.slug}>
                      {subject.title} ({subject.childrenCount} Chương)
                    </option>
                  ))}
                </select>
              </div>
            </div>
            <div className="col">
              <div className="form-group">
                <label htmlFor="chapter">Chương</label>
                <select
                  disabled={fields.subject == ""}
                  onChange={handleChapterChange}
                  value={fields.chapter}
                  className="form-control"
                  id="chapter"
                >
                  <option value="">LỰA CHỌN</option>
                  {chapters.map((chapter, index) => (
                    <option key={index} value={chapter.slug}>
                      {chapter.order} {chapter.title}
                    </option>
                  ))}
                </select>
              </div>
            </div>
          </div>

          <div className="row">
            <div className="col-9">
              <div className="form-group">
                <label htmlFor="title">Tiêu đề</label>
                <input
                  value={fields.title}
                  onChange={handleFieldChange}
                  type="text"
                  className="form-control"
                  id="title"
                />
              </div>
            </div>
            <div className="col-3">
              <div className="form-group">
                <label htmlFor="order">Thứ tự</label>
                <input
                  value={fields.order}
                  onChange={handleFieldChange}
                  type="number"
                  className="form-control"
                  id="order"
                />
              </div>
            </div>
          </div>

          <div className="form-group">
            <label htmlFor="caption">Tóm tắt</label>
            <textarea
              value={fields.caption}
              onChange={handleFieldChange}
              id="caption"
              className="form-control"
              rows="5"
            />
          </div>

          <div className="form-inline">
            <button onClick={handleFileUpload} className="btn btn-primary mb-2">
              Tải lên
            </button>
            <div className="form-group mx-sm-3 mb-2" style={{ flex: 1 }}>
              <div className="custom-file">
                <input
                  required
                  type="file"
                  className="custom-file-input"
                  name="file"
                  onChange={handleFileChange}
                  accept="application/msword, .docx"
                />
                <label className="custom-file-label" htmlFor="file">
                  {selectedFile?.name || "Tải lên Tài liệu"}
                </label>
              </div>
            </div>
          </div>

          <div className="form-group">
            <label htmlFor="content">Nội dung</label>
            <textarea
              id="content"
              className="form-control"
              rows="12"
              value={fields.content}
              onChange={handleFieldChange}
            />
          </div>

          {loaddingUpload ? (
            <Loadding />
          ) : (
            <>
              {fields.content.trim() != "" && (
                <button
                  onClick={handleContentUpload}
                  className="btn btn-primary"
                >
                  Đăng bài
                </button>
              )}
            </>
          )}
        </div>

        {messages && (
          <ul className="messagelist">
            {messages.map((message, index) => (
              <li key={index} className={message?.tags ?? ""}>
                {message | capfirst}
              </li>
            ))}
          </ul>
        )}
      </div>
    </>
  );
}

root.render(<App />);
