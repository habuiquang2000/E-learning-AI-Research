const { useState, useEffect, useLayoutEffect, useMemo } = React;

const root = ReactDOM.createRoot(document.getElementById("csv-upload"));

const convert_string_to_bool = (data) =>
  typeof data === "boolean" ? data : JSON.parse(data?.toLowerCase() || "false");

const Loadding = () => {
  return (
    <div className="text-center">
      <h1>ĐANG TẢI...</h1>
    </div>
  );
};

const CSVSelector = ({ onChange }) => {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = async (e) => {
    if (e.target.files) {
      try {
        const file = e.target.files[0];
        setSelectedFile(file);

        // 1. create url from the file
        const fileUrl = URL.createObjectURL(file);

        // 2. use fetch API to read the file
        const response = await fetch(fileUrl);

        // 3. get the text from the response
        const text = await response.text();

        // 4. split the text by newline
        const lines = text.split("\n");

        // 5. map through all the lines and split each line by comma.
        const lineArrs = lines.map((line) => line.split(";"));

        const headers = lineArrs[0];
        const rows = lineArrs.slice(1);

        const result = rows.map((row) => {
          const obj = {};
          row.map((cell, index) => {
            obj[headers[index].trim()] = cell;
          });
          return obj;
        });

        // 6. call the onChange event
        onChange(result);
      } catch (error) {
        console.error(error);
      }
    }
  };

  return (
    <>
      <div className="custom-file">
        <input
          required
          type="file"
          className="custom-file-input"
          id="image"
          name="file"
          onChange={handleFileChange}
          // accept=".csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel"
          accept=".csv"
        />
        <label className="custom-file-label" htmlFor="image">
          {selectedFile?.name || "Tải lên danh sách huấn luyện"}
        </label>
      </div>
    </>
  );
};

function App() {
  const [loaddingUpload, setLoaddingUpload] = useState(false);

  const [answers, setAnswers] = useState([]);
  const [count, setCount] = useState(0);
  const [messages, setMessages] = useState([]);

  const handleCSVChange = (answer) => {
    setAnswers(answer);
    setCount(answer.length);
  };
  const handleChangeAnswers = (event, index, field) => {
    const value = event.target.value;

    setAnswers((answersPre) =>
      answersPre.map((obj, objIndex) => {
        if (objIndex == index) return { ...obj, [field]: value };
        return obj;
      })
    );
  };

  const handleAnswersUpload = () => {
    setLoaddingUpload(true);

    postAnswerTrain(answers)
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

  const handleFieldAdd = () => {
    setAnswers((prev) => [
      ...prev,
      {
        question: "",
        content: "",
        keyword: "",
      },
    ]);
  };

  return (
    <>
      <CSVSelector onChange={handleCSVChange} />
      <div className="module" id="changelist">
        <div className="results">
          <table id="result_list">
            <thead>
              <tr>
                <th scope="col" className="th_custom">
                  <div className="text">Câu hỏi</div>
                  <div className="clear"></div>
                </th>
                <th scope="col" className="th_custom">
                  <div className="text">Câu trả lời</div>
                  <div className="clear"></div>
                </th>
                <th scope="col" className="th_custom">
                  <div className="text">Từ khóa</div>
                  <div className="clear"></div>
                </th>
              </tr>
            </thead>

            <tbody>
              {answers.map((answer, index) => (
                <tr className="row1" key={index}>
                  {Object.keys(answer).map((k, kIndex) => (
                    <td className="th_custom" key={kIndex}>
                      <input
                        className="w-100 form-control"
                        type="text"
                        value={answer[k]}
                        onChange={(event) =>
                          handleChangeAnswers(event, index, k)
                        }
                      />
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
          <button
            onClick={handleFieldAdd}
            type="button"
            class="btn btn-secondary w-100 font-weight-bold"
          >
            +
          </button>
          {loaddingUpload ? (
            <Loadding />
          ) : (
            <>
              {answers.length != 0 && (
                <button
                  onClick={handleAnswersUpload}
                  className="mt-3 btn btn-primary w-100 font-weight-bold"
                >
                  Huấn luyện
                </button>
              )}
            </>
          )}
        </div>
        {count != 0 && <p className="paginator">{count} Kết quả</p>}

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
