
# uygulama içi karanlık mod değişim kodları

def set_dark_mode_stylesheet():
    stylesheet = """
        QWidget {
            background-color: #222222;
            color: #F8F8F8;
        }
        
        /* Ana widget arka planı */
        QWidget#mainPage {
            background-color: #1E1E1E;
        }
        
        /* ComboBox arka planı */
        QComboBox {
            background-color: #2E2E2E;
            border: 1px solid #4F4F4F;
        }
        
        /* PushButton arka planı */
        QPushButton {
            background-color: #2E2E2E;
            border: 1px solid #4F4F4F;
            color: #F0F0F0;
        }
        
        /* Tablo arka planı */
        QTableWidget {
            background-color: #2E2E2E;
            border: 1px solid #4F4F4F;
            color: #F0F0F0;
        }
        
        /* Tablo başlık arka planı */
        QHeaderView::section {
            background-color: #3E3E3E;
            color: #F0F0F0;
            border: 1px solid #4F4F4F;
        }
        
        /* Tablo içeriği arka planı */
        QTableView QTableCornerButton::section {
            background-color: #3E3E3E;
            border: 1px solid #4F4F4F;
        }
    """
    return stylesheet
# :)