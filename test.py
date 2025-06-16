from fpdf import FPDF

# Create a custom PDF class
class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        self.add_page()
        self.set_font("Arial", size=12)

    def section_title(self, title):
        self.set_font("Arial", "B", 14)
        self.set_text_color(0, 0, 128)
        self.cell(0, 10, title, ln=True)
        self.set_font("Arial", size=12)
        self.set_text_color(0, 0, 0)

    def add_tcode_table(self, tcode_list):
        col_width_code = 60  # Wider for long T-Codes
        col_width_desc = 130  # Adjusted accordingly

        self.set_fill_color(220, 220, 220)
        self.set_font("Arial", "B", 12)
        self.cell(col_width_code, 10, "T-Code", 1, 0, "C", 1)
        self.cell(col_width_desc, 10, "Description", 1, 1, "C", 1)
        self.set_font("Arial", "", 11)

        for code, desc in tcode_list:
            self.cell(col_width_code, 8, code, 1)
            self.cell(col_width_desc, 8, desc, 1)
            self.ln()


# T-Codes Dictionary (truncated for space in this snippet, use your full dictionary)
sap_tcodes_full = {
    "1. General / Basis / Administration": [
        ("SE80", "Object Navigator"), ("SE38", "ABAP Editor"), ("SE11", "Data Dictionary"),
        ("SE37", "Function Module"), ("SE24", "Class Builder"), ("SE93", "Transaction Codes"),
        ("ST22", "Dump Analysis"), ("SM37", "Job Monitoring"), ("SM36", "Schedule Job"),
        ("SM12", "Locked Entries"), ("SM21", "System Logs"), ("SM59", "RFC Destinations"),
        ("ST01", "Trace Authorization"), ("ST03N", "Workload Analysis"), ("SU01", "User Maintenance"),
        ("SU10", "Mass User Change"), ("SU53", "Authorization Error Analysis"), ("PFCG", "Role Maintenance"),
        ("SCC1", "Client Copy"), ("SCC4", "Client Settings"), ("SNOTE", "SAP Notes Implementation"),
        ("DB02", "DB Space Overview"), ("SPRO", "Customizing Implementation Guide"), ("SOBJ", "Repository Objects"),
        ("SA38", "Run Program"), ("OSS1", "SAP Online Support"), ("WE02", "IDoc Display"),
        ("BD87", "Reprocess IDocs")
    ],
    "2. FI - Financial Accounting": [
        ("FB50", "G/L Posting"), ("F-02", "Manual Posting"), ("F-03", "Clear G/L Account"),
        ("F-04", "Post with Clearing"), ("FB01", "Post Document"), ("FB08", "Reverse Document"),
        ("F110", "Automatic Payment Run"), ("F-53", "Outgoing Payments"), ("F-28", "Incoming Payments"),
        ("FB60", "Vendor Invoice"), ("FB65", "Vendor Credit Memo"), ("FB70", "Customer Invoice"),
        ("FB75", "Customer Credit Memo"), ("FS00", "G/L Master Record"), ("FBL1N", "Vendor Line Items"),
        ("FBL3N", "G/L Line Items"), ("FBL5N", "Customer Line Items"), ("F.01", "Financial Statements"),
        ("F.13", "Automatic Clearing"), ("OB52", "Posting Periods"), ("OBYC", "Automatic Postings"),
        ("S_ALR_87012168", "Vendor Payments Report"), ("S_ALR_87012301", "Customer Analysis"),
        ("S_P99_41000099", "Tax Report")
    ],
    "3. MM - Materials Management": [
        ("MM01", "Create Material"), ("MM02", "Change Material"), ("MM03", "Display Material"),
        ("ME11", "Create Info Record"), ("ME21N", "Create PO"), ("ME22N", "Change PO"),
        ("ME23N", "Display PO"), ("ME31K", "Create Contract"), ("ME51N", "Create PR"),
        ("ME52N", "Change PR"), ("ME53N", "Display PR"), ("ME54N", "Release PR"),
        ("MIGO", "Goods Movement"), ("MB1A", "Goods Issue"), ("MB1B", "Transfer Posting"),
        ("MB1C", "Initial Stock"), ("MIRO", "Enter Invoice"), ("MR8M", "Cancel Invoice"),
        ("MRBR", "Release Blocked Invoice"), ("MB03", "Display Mat. Doc."), ("ME2L", "PO by Vendor"),
        ("ME2M", "PO by Material"), ("ME2K", "PO by Account"), ("ME3M", "Outline Agreements by Material"),
        ("ME9F", "Print PO"), ("MB51", "Material Document List"), ("MMBE", "Stock Overview"),
        ("MB5T", "Stock in Transit"), ("OMJJ", "Movement Type Configuration"), ("ME80FN", "PO History Report")
    ],
    "4. SD - Sales and Distribution": [
        ("VA01", "Create Sales Order"), ("VA02", "Change Sales Order"), ("VA03", "Display Sales Order"),
        ("VA05", "List Sales Orders"), ("VA21", "Create Quotation"), ("VA22", "Change Quotation"),
        ("VA23", "Display Quotation"), ("VA31", "Create Scheduling Agreement"), ("VA41", "Create Contract"),
        ("VD01", "Create Customer (Sales)"), ("XD01", "Create Customer (Centrally)"), ("VD03", "Display Customer"),
        ("VL01N", "Create Delivery"), ("VL02N", "Change Delivery"), ("VL03N", "Display Delivery"),
        ("VF01", "Create Billing"), ("VF02", "Change Billing"), ("VF03", "Display Billing"),
        ("VFX3", "Release Billing"), ("VK11", "Create Condition"), ("VK12", "Change Condition"),
        ("VK13", "Display Condition"), ("VK31", "Create Pricing Conditions (Mass)"),
        ("VOTXN", "Output Types"), ("VT01N", "Create Shipment"), ("VKM3", "Credit Management"),
        ("V.01", "Sales Summary Report"), ("VLPOD", "Proof of Delivery")
    ],
    "5. PP - Production Planning": [
        ("MD01", "Total Planning"), ("MD02", "Single Item Planning"), ("MD04", "Stock/Requirement List"),
        ("MD05", "MRP List"), ("CO01", "Create Production Order"), ("CO02", "Change Production Order"),
        ("CO03", "Display Production Order"), ("COR1", "Create Process Order"), ("COR2", "Change Process Order"),
        ("COR3", "Display Process Order"), ("MF47", "Convert Planned Order"), ("MF60", "Rough-Cut Planning"),
        ("MB31", "Goods Receipt for Order"), ("MB1A", "Goods Issue"), ("C001", "Create Work Center"),
        ("CR01", "Work Center Creation"), ("CA01", "Create Routing"), ("CA02", "Change Routing"),
        ("CS01", "Create BOM"), ("CS02", "Change BOM"), ("CS03", "Display BOM"), ("MF50", "Planning Table"),
        ("CM01", "Capacity Planning"), ("MF65", "Planning Evaluation")
    ],
    "6. PM - Plant Maintenance": [
        ("IW21", "Create Notification"), ("IW22", "Change Notification"), ("IW23", "Display Notification"),
        ("IW31", "Create Order"), ("IW32", "Change Order"), ("IW33", "Display Order"),
        ("IE01", "Create Equipment"), ("IE02", "Change Equipment"), ("IE03", "Display Equipment"),
        ("IL01", "Create Functional Location"), ("IL02", "Change Functional Location"),
        ("IL03", "Display Functional Location"), ("IP01", "Create Maintenance Plan"),
        ("IP02", "Change Maintenance Plan"), ("IP03", "Display Maintenance Plan"), ("IP10", "Schedule Plan"),
        ("IH01", "Structure Display"), ("IW38", "List Orders"), ("IW39", "Notification List")
    ],
    "7. Reporting and Analytics": [
        ("MB52", "List Warehouse Stock"), ("ME2N", "Purchase Orders by Number"), ("ME80FN", "PO History"),
        ("S_ALR_87012082", "Cost Center Plan/Actual"), ("S_ALR_87012357", "G/L Account Balances"),
        ("S_ALR_87012168", "Vendor Payment History"), ("S_ALR_87012301", "Customer Receivables"),
        ("KSB1", "Cost Center Actual Line Items"), ("KOB1", "Internal Orders Actual Line Items"),
        ("KE30", "Profitability Analysis"), ("MB5B", "Stock for Posting Date"),
        ("MRP_CTRL_CHECK", "MRP Controller Worklist"), ("SE16N", "Table Browser (new SE16)")
    ],
    "8. Smart Forms": [
        ("SMARTFORMS", "Create/Change Smart Forms"),
        ("SMARTSTYLES", "Define Smart Styles"),
        ("SFTRACE", "Trace tool for Smart Forms"),
        ("SFDEBUG", "Debug Smart Forms"),
        ("SE71", "SAPscript Form Painter"),
        ("SE78", "Upload Graphics (logos)"),
        ("NACE", "Output Determination"),
        ("SFPFPATH", "Maintain Smart Form Path"),
        ("SPAD", "Spool Administration"),
        ("SP01", "Output Requests"),
        ("ST22", "Dump Analyzer"),
        ("SE93", "Maintain Transaction Codes"),
    ],
    "9. Adobe Forms": [
        ("SFP", "Adobe Form Builder"),
        ("SFP_TEST", "Test Adobe Form"),
        ("SFP_TRACE", "Trace Adobe Form Execution"),
        ("SFPADM", "Adobe Form Runtime Admin"),
        ("SFP_FUNCTION_MODULE", "Generated FM for Adobe Form"),
        ("SFP_CMP", "Compare Adobe Forms"),
        ("SE78", "Upload Form Images"),
        ("SPAD", "Spool Admin"),
        ("SP01", "Check Printed Form"),
        ("SE24", "Adobe Form Classes"),
        ("SE11", "Form Structures"),
    ],
    "10. OData Services (SAP Gateway)": [
        ("SEGW", "OData Service Builder"),
        ("/IWFND/MAINT_SERVICE", "Manage OData Services"),
        ("/IWBEP/REG_SERVICE", "Register Backend Services"),
        ("/IWFND/GW_CLIENT", "OData Client Tester"),
        ("SICF", "Activate HTTP Services"),
        ("SMICM", "HTTP Server Monitor"),
        ("SU53", "Authorization Check"),
        ("SU01", "User Maintenance"),
        ("PFCG", "Role Maintenance"),
        ("ST22", "Dump Analyzer"),
        ("ST05", "SQL Trace"),
        ("SE24", "Generated Classes"),
        ("SE80", "ABAP Repository Explorer"),
        ("/IWFND/TRACES", "Gateway Trace Tool"),
    ],
    "11. CDS Views (Core Data Services)": [
        ("SE11", "View CDS Tables/SQL Views"),
        ("SE80", "Repository Explorer"),
        ("ST05", "SQL Performance Trace"),
        ("RSRT", "Run CDS Analytical Query"),
        ("SADT_START", "ADT Launcher"),
        ("SACM", "CDS View Authorization"),
        ("SU24", "Authorization Objects"),
        ("SUIM", "User Info System"),
        ("SM30", "Maintain Config Tables"),
        ("SE93", "Create T-Code for CDS Query"),
        ("SE16N", "Explore CDS Data"),
        ("RSRVT", "Check InfoProvider Consistency"),
        ("RSO2", "Maintain BW InfoObjects"),
        ("RSEG", "Test CDS Logic"),
    ]
}

# Generate PDF
pdf = PDF()

for section, tcode_list in sap_tcodes_full.items():
    pdf.section_title(section)
    pdf.add_tcode_table(tcode_list)
    pdf.ln(5)

# Save to your desired path (you can change the path)
pdf.output("Full_SAP_ERP_TCodes_Reference.pdf")

print("✅ PDF generated: Full_SAP_ERP_TCodes_Reference.pdf")
