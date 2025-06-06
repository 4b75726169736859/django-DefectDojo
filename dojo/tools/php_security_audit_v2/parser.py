import json
import math

from dojo.models import Finding


class PhpSecurityAuditV2Parser:
    def get_scan_types(self):
        return ["PHP Security Audit v2"]

    def get_label_for_scan_types(self, scan_type):
        return scan_type

    def get_description_for_scan_types(self, scan_type):
        return "Import PHP Security Audit v2 Scan in JSON format."

    def get_findings(self, filename, test):
        tree = filename.read()
        try:
            data = json.loads(str(tree, "utf-8"))
        except Exception:
            data = json.loads(tree)
        dupes = {}

        for filepath, report in list(data["files"].items()):
            errors = report.get("errors") or 0
            warns = report.get("warnings") or 0
            if errors + warns > 0:
                for issue in report["messages"]:
                    title = issue["source"]

                    findingdetail = "Filename: " + filepath + "\n"
                    findingdetail += "Line: " + str(issue["line"]) + "\n"
                    findingdetail += "Column: " + str(issue["column"]) + "\n"
                    findingdetail += "Rule Source: " + issue["source"] + "\n"
                    findingdetail += "Details: " + issue["message"] + "\n"

                    sev = PhpSecurityAuditV2Parser.get_severity_word(
                        issue["severity"],
                    )

                    dupe_key = (
                        title
                        + filepath
                        + str(issue["line"])
                        + str(issue["column"])
                    )

                    if dupe_key in dupes:
                        find = dupes[dupe_key]
                    else:
                        dupes[dupe_key] = True

                        find = Finding(
                            title=title,
                            test=test,
                            description=findingdetail,
                            severity=sev.title(),
                            file_path=filepath,
                            line=issue["line"],
                            static_finding=True,
                            dynamic_finding=False,
                        )

                        dupes[dupe_key] = find
                        findingdetail = ""

        return list(dupes.values())

    @staticmethod
    def get_severity_word(severity):
        sev = math.ceil(severity / 2)

        if sev == 5:
            return "Critical"
        if sev == 4:
            return "High"
        if sev == 3:
            return "Medium"
        return "Low"
