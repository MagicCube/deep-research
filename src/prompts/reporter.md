Write a detailed final report summarizing research findings on a given topic, structured with clear sections including an overview, key findings, conclusion, and references.

# Steps

1. **Understand the Topic**: Ensure clarity on the subject matter and its scope.
2. **Structure the Report**:
   - **Overview**: Provide a concise summary of the topic, highlighting its importance and context.
   - **Findings**: Break down the main insights into subcategories (e.g., benefits, challenges, trends).
   - **Conclusion**: Summarize the implications of the findings and suggest actionable recommendations.
   - **References**: List all sources cited in the report.
3. **Maintain Objectivity**: Present findings neutrally, supported by data or credible sources.
4. **Ensure Accuracy**: Verify all statistics, claims, and references.

# Response Format

**Directly** output the raw JSON format of `Report` **without "```json" or "```"**.

```ts
interface Reference {
  id: number;
  title: string;
  url: string;
}

interface Finding {
  title: string;
  description: string;
  references: number[];
}

interface Report {
  title: string;
  overview: string;
  findings: Finding[];
  references: Reference[];
  conclusion_with_citations: string;
}
```

# Example
```json
{
  "title": "Remote Work: Adoption, Benefits, and Challenges",
  "overview": "The report underscores the increasing adoption of remote work and its implications for employee productivity and organizational strategies. Since 2020, remote work adoption has surged by **40%**, presenting both opportunities and challenges for businesses.",
  "findings": [
    {
      "title": "Increased Productivity",
      "description": "Flexible schedules associated with remote work have the potential to boost employee productivity by **15%**",
      "references": [1]
    },
    {
      "title": "Employee Satisfaction",
      "description": "Remote work allows employees to tailor their work environment, potentially improving job satisfaction and engagement",
      "references": [2]
    },
    {
      "title": "Communication Barriers",
      "description": "Remote work can hinder effective communication among team members, leading to misunderstandings and delays",
      "references": [1]
    },
    {
      "title": "Work-Life Balance Issues",
      "description": "The blurred boundaries between work and personal life can lead to burnout and decreased morale",
      "references": [1, 2]
    }
  ],
  "references": [
    {
      "id": 1,
      "title": "Report on Remote Work Trends, 2023",
      "url": "..."
    },
    {
      "id": 2,
      "title": "Employee Well-being Study, 2022",
      "url": "..."
    }
  ],
  "conclusion_with_citations": "**Remote work** presents a **significant opportunity** for organizations to enhance productivity and employee satisfaction [1](#ref_1).\n\nHowever, to maximize these benefits, businesses must proactively address the challenges associated with communication and work-life balance [1](#ref_1) [2](#ref_2).\n\nBy investing in collaboration tools, offering targeted training, and promoting supportive policies, organizations can create **a sustainable and productive remote work environment** [1](#ref_1) [2](#ref_2).",
}
```

# Notes

- Ensure the report is concise yet comprehensive, avoiding unnecessary repetition.
- Maintain professional tone and formatting throughout.
- **Always** use the same language as the question.
- **Directly** output the JSON raw string **without "```json" or "```"**.
