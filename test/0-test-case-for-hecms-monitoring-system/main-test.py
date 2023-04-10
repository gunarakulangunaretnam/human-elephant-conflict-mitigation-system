from datetime import datetime
from html import escape
import utilities

# Run the tests
test_login_failed = utilities.test_login_failed()
test_login_succeed = utilities.test_login_succeed()
test_login_alarm_option = utilities.test_alarm_options()
test_start_processing_video_selector = utilities.test_select_video_and_start_processing()
test_stop_processing = utilities.test_stop_processing()

# Define the table contents
table_contents = [
    ('Test Login Failed', test_login_failed),
    ('Test Login Succeeded', test_login_succeed),
    ('Test Alarm Options', test_login_alarm_option),
    ('Test Broswe Option', test_start_processing_video_selector),
    ('Test Video Path Field', test_start_processing_video_selector),
    ('Test Start Processing', test_start_processing_video_selector),
    ('Test Stop Processing', test_stop_processing)
]

# Define the HTML template
html_template = '''
<html>
<head>
    <title>HEMCS Monitoring System Test Results</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1>HEMCS Monitoring System Test Results</h1>
        <h3>{test_result}</h3>
        <table class="table">
            <thead>
                <tr>
                    <th>Test Name</th>
                    <th>Result</th>
                </tr>
            </thead>
            <tbody>
                {table_rows}
            </tbody>
        </table>
        <p>Testing started at {start_time} on {start_date} and completed at {end_time} on {end_date}</p>
    </div>
</body>
</html>
'''

# Generate the table rows
table_rows = ''
for test_name, test_result in table_contents:
    row_class = 'success' if test_result else 'danger'
    row_contents = f'<td>{escape(test_name)}</td><td>{test_result}</td>'
    table_rows += f'<tr class="{row_class}">{row_contents}</tr>'

# Determine the overall test result
overall_test_result = 'Passed' if all(table_result for _, table_result in table_contents) else 'Failed'

# Get the start and end times
start_time = datetime.now().strftime('%H:%M:%S')
start_date = datetime.now().strftime('%Y-%m-%d')
end_time = datetime.now().strftime('%H:%M:%S')
end_date = datetime.now().strftime('%Y-%m-%d')

# Generate the final HTML
final_html = html_template.format(
    test_result=overall_test_result,
    table_rows=table_rows,
    start_time=start_time,
    start_date=start_date,
    end_time=end_time,
    end_date=end_date
)

# Write the HTML to a file
with open(f'results/{end_date}-{end_time.replace(":", "-")}-test-results.html', 'w') as f:
    f.write(final_html)
