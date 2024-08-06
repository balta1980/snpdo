# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inicio.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(723, 376)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/prefijo/rect841.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget {\n"
"   font: 10pt;\n"
"    \n"
"}\n"
"QDateEdit{}\n"
"QDateEdit:focus{background-color: rgb(255, 255, 127);}\n"
"\n"
"QTextEdit{}\n"
"QTextEdit:focus{background-color: rgb(255, 255, 127);}\n"
"\n"
"QPlainTextEdit{}\n"
"QPlainTextEdit:focus{background-color: rgb(255, 255, 127);}\n"
"\n"
"QLineEdit{}\n"
"QLineEdit:focus{background-color: rgb(255, 255, 127);}\n"
"\n"
"QComboBox{}\n"
"QComboBox:focus{background-color: rgb(255, 255, 127);}\n"
"\n"
"QDoubleSinBox{}\n"
"QDoubleSpinBox:focus{background-color: rgb(255, 255, 127);}\n"
"\n"
"QTimeEdit{}\n"
"QTimeEdit:focus{background-color: rgb(255, 255, 127);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mdiArea.sizePolicy().hasHeightForWidth())
        self.mdiArea.setSizePolicy(sizePolicy)
        self.mdiArea.setMaximumSize(QtCore.QSize(12000000, 12000000))
        self.mdiArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mdiArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mdiArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.mdiArea.setViewMode(QtWidgets.QMdiArea.SubWindowView)
        self.mdiArea.setDocumentMode(False)
        self.mdiArea.setObjectName("mdiArea")
        self.verticalLayout.addWidget(self.mdiArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 723, 20))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuDefiniciones = QtWidgets.QMenu(self.menubar)
        self.menuDefiniciones.setObjectName("menuDefiniciones")
        self.menuTrabajadores = QtWidgets.QMenu(self.menubar)
        self.menuTrabajadores.setObjectName("menuTrabajadores")
        self.menuVariaciones = QtWidgets.QMenu(self.menubar)
        self.menuVariaciones.setObjectName("menuVariaciones")
        self.menuHoras_extraordinarias = QtWidgets.QMenu(self.menuVariaciones)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("iconos/hora_extra.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuHoras_extraordinarias.setIcon(icon1)
        self.menuHoras_extraordinarias.setObjectName("menuHoras_extraordinarias")
        self.menuInasistencias = QtWidgets.QMenu(self.menuVariaciones)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("iconos/falta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuInasistencias.setIcon(icon2)
        self.menuInasistencias.setObjectName("menuInasistencias")
        self.menuRegistro_de_comisi_n = QtWidgets.QMenu(self.menuVariaciones)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("iconos/or.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuRegistro_de_comisi_n.setIcon(icon3)
        self.menuRegistro_de_comisi_n.setObjectName("menuRegistro_de_comisi_n")
        self.menuOtras_remuneraciones = QtWidgets.QMenu(self.menuVariaciones)
        self.menuOtras_remuneraciones.setIcon(icon3)
        self.menuOtras_remuneraciones.setObjectName("menuOtras_remuneraciones")
        self.menuRemuneraci_n_otros_empleadores = QtWidgets.QMenu(self.menuVariaciones)
        self.menuRemuneraci_n_otros_empleadores.setIcon(icon3)
        self.menuRemuneraci_n_otros_empleadores.setObjectName("menuRemuneraci_n_otros_empleadores")
        self.menuIndemnizaciones_laborales = QtWidgets.QMenu(self.menuVariaciones)
        self.menuIndemnizaciones_laborales.setIcon(icon3)
        self.menuIndemnizaciones_laborales.setObjectName("menuIndemnizaciones_laborales")
        self.menuBeneficios = QtWidgets.QMenu(self.menubar)
        self.menuBeneficios.setObjectName("menuBeneficios")
        self.menuN_mina = QtWidgets.QMenu(self.menubar)
        self.menuN_mina.setObjectName("menuN_mina")
        self.menuReportes = QtWidgets.QMenu(self.menubar)
        self.menuReportes.setObjectName("menuReportes")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        self.menuVentana = QtWidgets.QMenu(self.menubar)
        self.menuVentana.setObjectName("menuVentana")
        self.menuCambiar_tema_2 = QtWidgets.QMenu(self.menuVentana)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("iconos/style.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuCambiar_tema_2.setIcon(icon4)
        self.menuCambiar_tema_2.setObjectName("menuCambiar_tema_2")
        self.menuUsuarios = QtWidgets.QMenu(self.menubar)
        self.menuUsuarios.setObjectName("menuUsuarios")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setAcceptDrops(False)
        self.dockWidget.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.dockWidgetContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 255, 368))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.cumple_mes = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cumple_mes.sizePolicy().hasHeightForWidth())
        self.cumple_mes.setSizePolicy(sizePolicy)
        self.cumple_mes.setObjectName("cumple_mes")
        self.verticalLayout_3.addWidget(self.cumple_mes)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.prox_per_vac = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.prox_per_vac.setObjectName("prox_per_vac")
        self.verticalLayout_3.addWidget(self.prox_per_vac)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.feriados_mes = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.feriados_mes.setObjectName("feriados_mes")
        self.verticalLayout_3.addWidget(self.feriados_mes)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.estatus_trab_info = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.estatus_trab_info.setObjectName("estatus_trab_info")
        self.verticalLayout_3.addWidget(self.estatus_trab_info)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)
        self.actionCerrar = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("iconos/shutdown_off_close_exit_15253.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCerrar.setIcon(icon5)
        self.actionCerrar.setObjectName("actionCerrar")
        self.actionPeriodos = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("iconos/product_document_file_1512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPeriodos.setIcon(icon6)
        self.actionPeriodos.setObjectName("actionPeriodos")
        self.actionD_as_No_laborables = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("iconos/calendar_office_day_1474.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionD_as_No_laborables.setIcon(icon7)
        self.actionD_as_No_laborables.setObjectName("actionD_as_No_laborables")
        self.actionDefinir_vacaciones = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("iconos/fir-tree_icon-icons.com_49161.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDefinir_vacaciones.setIcon(icon8)
        self.actionDefinir_vacaciones.setObjectName("actionDefinir_vacaciones")
        self.actionDefinir_salario_m_nimo = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("iconos/salmin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDefinir_salario_m_nimo.setIcon(icon9)
        self.actionDefinir_salario_m_nimo.setObjectName("actionDefinir_salario_m_nimo")
        self.actionDefinir_tabla_ISLR = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("iconos/islr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDefinir_tabla_ISLR.setIcon(icon10)
        self.actionDefinir_tabla_ISLR.setObjectName("actionDefinir_tabla_ISLR")
        self.actionDefinici_n_de_riesgo_laboral = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("iconos/tss.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDefinici_n_de_riesgo_laboral.setIcon(icon11)
        self.actionDefinici_n_de_riesgo_laboral.setObjectName("actionDefinici_n_de_riesgo_laboral")
        self.actionListado_de_trabajadores = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("iconos/x-office-address-book_35984.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionListado_de_trabajadores.setIcon(icon12)
        self.actionListado_de_trabajadores.setObjectName("actionListado_de_trabajadores")
        self.actionPlano = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("iconos/sol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlano.setIcon(icon13)
        self.actionPlano.setObjectName("actionPlano")
        self.actionObscuro = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("iconos/luna.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionObscuro.setIcon(icon14)
        self.actionObscuro.setObjectName("actionObscuro")
        self.actionCascada = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("iconos/cascada.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCascada.setIcon(icon15)
        self.actionCascada.setObjectName("actionCascada")
        self.actionMosaico = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("iconos/mosaico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMosaico.setIcon(icon16)
        self.actionMosaico.setObjectName("actionMosaico")
        self.actionClaro = QtWidgets.QAction(MainWindow)
        self.actionClaro.setIcon(icon13)
        self.actionClaro.setObjectName("actionClaro")
        self.actionObscuro_2 = QtWidgets.QAction(MainWindow)
        self.actionObscuro_2.setIcon(icon14)
        self.actionObscuro_2.setObjectName("actionObscuro_2")
        self.actionConfigurar_correo_de_n_mina = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("iconos/correo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConfigurar_correo_de_n_mina.setIcon(icon17)
        self.actionConfigurar_correo_de_n_mina.setObjectName("actionConfigurar_correo_de_n_mina")
        self.actionBloquear = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("iconos/bloquear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBloquear.setIcon(icon18)
        self.actionBloquear.setObjectName("actionBloquear")
        self.actionRegistro_de_salario_nuevo = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("iconos/salario_nuevo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRegistro_de_salario_nuevo.setIcon(icon19)
        self.actionRegistro_de_salario_nuevo.setObjectName("actionRegistro_de_salario_nuevo")
        self.actionRegistro_de_dotaci_n = QtWidgets.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("iconos/dota.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRegistro_de_dotaci_n.setIcon(icon20)
        self.actionRegistro_de_dotaci_n.setObjectName("actionRegistro_de_dotaci_n")
        self.actionCostos_laborales = QtWidgets.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("iconos/legal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCostos_laborales.setIcon(icon21)
        self.actionCostos_laborales.setObjectName("actionCostos_laborales")
        self.actionBeneficios_seg_n_ley = QtWidgets.QAction(MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("iconos/beneficios.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBeneficios_seg_n_ley.setIcon(icon22)
        self.actionBeneficios_seg_n_ley.setObjectName("actionBeneficios_seg_n_ley")
        self.actionN_mina_quincenal = QtWidgets.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("iconos/nomina.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionN_mina_quincenal.setIcon(icon23)
        self.actionN_mina_quincenal.setObjectName("actionN_mina_quincenal")
        self.actionLiquidaci_n = QtWidgets.QAction(MainWindow)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("iconos/liquidacion.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLiquidaci_n.setIcon(icon24)
        self.actionLiquidaci_n.setObjectName("actionLiquidaci_n")
        self.actionPago_utilidades = QtWidgets.QAction(MainWindow)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap("iconos/utilidades.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPago_utilidades.setIcon(icon25)
        self.actionPago_utilidades.setObjectName("actionPago_utilidades")
        self.actionN_mina_extraordinaria = QtWidgets.QAction(MainWindow)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap("iconos/especial.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionN_mina_extraordinaria.setIcon(icon26)
        self.actionN_mina_extraordinaria.setObjectName("actionN_mina_extraordinaria")
        self.actionFormato_de_asistencia = QtWidgets.QAction(MainWindow)
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap("iconos/formato.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFormato_de_asistencia.setIcon(icon27)
        self.actionFormato_de_asistencia.setObjectName("actionFormato_de_asistencia")
        self.actionInforme_TSS = QtWidgets.QAction(MainWindow)
        self.actionInforme_TSS.setIcon(icon11)
        self.actionInforme_TSS.setObjectName("actionInforme_TSS")
        self.actionN_mina_Individual = QtWidgets.QAction(MainWindow)
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap("iconos/nom_ind.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionN_mina_Individual.setIcon(icon28)
        self.actionN_mina_Individual.setObjectName("actionN_mina_Individual")
        self.actionVer_info = QtWidgets.QAction(MainWindow)
        self.actionVer_info.setCheckable(True)
        self.actionVer_info.setChecked(True)
        self.actionVer_info.setObjectName("actionVer_info")
        self.actionRegistro_de_salario_por_lote = QtWidgets.QAction(MainWindow)
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap("iconos/salario_lote.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRegistro_de_salario_por_lote.setIcon(icon29)
        self.actionRegistro_de_salario_por_lote.setObjectName("actionRegistro_de_salario_por_lote")
        self.actionDatos_de_la_sociedad = QtWidgets.QAction(MainWindow)
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap("iconos/sociedad.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDatos_de_la_sociedad.setIcon(icon30)
        self.actionDatos_de_la_sociedad.setObjectName("actionDatos_de_la_sociedad")
        self.actionListado_de_usuarios = QtWidgets.QAction(MainWindow)
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap("iconos/usuarios.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionListado_de_usuarios.setIcon(icon31)
        self.actionListado_de_usuarios.setObjectName("actionListado_de_usuarios")
        self.actionListado_de_nacionalidades = QtWidgets.QAction(MainWindow)
        self.actionListado_de_nacionalidades.setIcon(icon11)
        self.actionListado_de_nacionalidades.setObjectName("actionListado_de_nacionalidades")
        self.actionResumen_de_recibos = QtWidgets.QAction(MainWindow)
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap("iconos/recibos_resumen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionResumen_de_recibos.setIcon(icon32)
        self.actionResumen_de_recibos.setObjectName("actionResumen_de_recibos")
        self.actionCarta_de_trabajo = QtWidgets.QAction(MainWindow)
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap("iconos/cartas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCarta_de_trabajo.setIcon(icon33)
        self.actionCarta_de_trabajo.setObjectName("actionCarta_de_trabajo")
        self.actionPantalla_completa = QtWidgets.QAction(MainWindow)
        icon34 = QtGui.QIcon()
        icon34.addPixmap(QtGui.QPixmap("iconos/full-screen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPantalla_completa.setIcon(icon34)
        self.actionPantalla_completa.setObjectName("actionPantalla_completa")
        self.actionRegistro_de_pr_stamo_adelanto = QtWidgets.QAction(MainWindow)
        icon35 = QtGui.QIcon()
        icon35.addPixmap(QtGui.QPixmap("iconos/prestamo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRegistro_de_pr_stamo_adelanto.setIcon(icon35)
        self.actionRegistro_de_pr_stamo_adelanto.setObjectName("actionRegistro_de_pr_stamo_adelanto")
        self.actionContenido_de_la_Ayuda = QtWidgets.QAction(MainWindow)
        icon36 = QtGui.QIcon()
        icon36.addPixmap(QtGui.QPixmap("iconos/ayuda.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionContenido_de_la_Ayuda.setIcon(icon36)
        self.actionContenido_de_la_Ayuda.setObjectName("actionContenido_de_la_Ayuda")
        self.actionAcerca_de_SNP = QtWidgets.QAction(MainWindow)
        icon37 = QtGui.QIcon()
        icon37.addPixmap(QtGui.QPixmap("iconos/acercade.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAcerca_de_SNP.setIcon(icon37)
        self.actionAcerca_de_SNP.setObjectName("actionAcerca_de_SNP")
        self.actionHaga_una_donaci_n = QtWidgets.QAction(MainWindow)
        icon38 = QtGui.QIcon()
        icon38.addPixmap(QtGui.QPixmap("iconos/paypal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHaga_una_donaci_n.setIcon(icon38)
        self.actionHaga_una_donaci_n.setObjectName("actionHaga_una_donaci_n")
        self.actionRegistro_de_horas_extra = QtWidgets.QAction(MainWindow)
        icon39 = QtGui.QIcon()
        icon39.addPixmap(QtGui.QPixmap("iconos/agrega.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRegistro_de_horas_extra.setIcon(icon39)
        self.actionRegistro_de_horas_extra.setObjectName("actionRegistro_de_horas_extra")
        self.actionListado_de_horas_extra = QtWidgets.QAction(MainWindow)
        icon40 = QtGui.QIcon()
        icon40.addPixmap(QtGui.QPixmap("iconos/listado.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionListado_de_horas_extra.setIcon(icon40)
        self.actionListado_de_horas_extra.setObjectName("actionListado_de_horas_extra")
        self.actionRegistro_de_inasistencia_2 = QtWidgets.QAction(MainWindow)
        self.actionRegistro_de_inasistencia_2.setIcon(icon39)
        self.actionRegistro_de_inasistencia_2.setObjectName("actionRegistro_de_inasistencia_2")
        self.actionListado_de_inasistencias = QtWidgets.QAction(MainWindow)
        self.actionListado_de_inasistencias.setIcon(icon40)
        self.actionListado_de_inasistencias.setObjectName("actionListado_de_inasistencias")
        self.actionRegistro_de_comisi_n = QtWidgets.QAction(MainWindow)
        self.actionRegistro_de_comisi_n.setIcon(icon39)
        self.actionRegistro_de_comisi_n.setObjectName("actionRegistro_de_comisi_n")
        self.actionListado_de_comisiones = QtWidgets.QAction(MainWindow)
        self.actionListado_de_comisiones.setIcon(icon40)
        self.actionListado_de_comisiones.setObjectName("actionListado_de_comisiones")
        self.actionRegistro_de_otra_remuneraci_n_2 = QtWidgets.QAction(MainWindow)
        self.actionRegistro_de_otra_remuneraci_n_2.setIcon(icon39)
        self.actionRegistro_de_otra_remuneraci_n_2.setObjectName("actionRegistro_de_otra_remuneraci_n_2")
        self.actionListado_otras_remun = QtWidgets.QAction(MainWindow)
        self.actionListado_otras_remun.setIcon(icon40)
        self.actionListado_otras_remun.setObjectName("actionListado_otras_remun")
        self.actionRegistro_rem_otro_empleador = QtWidgets.QAction(MainWindow)
        self.actionRegistro_rem_otro_empleador.setIcon(icon39)
        self.actionRegistro_rem_otro_empleador.setObjectName("actionRegistro_rem_otro_empleador")
        self.actionListado_rem_otro_empleador = QtWidgets.QAction(MainWindow)
        self.actionListado_rem_otro_empleador.setIcon(icon40)
        self.actionListado_rem_otro_empleador.setObjectName("actionListado_rem_otro_empleador")
        self.actionGuardar_BD_como = QtWidgets.QAction(MainWindow)
        icon41 = QtGui.QIcon()
        icon41.addPixmap(QtGui.QPixmap("iconos/exportar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGuardar_BD_como.setIcon(icon41)
        self.actionGuardar_BD_como.setObjectName("actionGuardar_BD_como")
        self.actionImportar_BD = QtWidgets.QAction(MainWindow)
        icon42 = QtGui.QIcon()
        icon42.addPixmap(QtGui.QPixmap("iconos/importar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImportar_BD.setIcon(icon42)
        self.actionImportar_BD.setObjectName("actionImportar_BD")
        self.actionRegistro_indemnizaciones = QtWidgets.QAction(MainWindow)
        self.actionRegistro_indemnizaciones.setIcon(icon39)
        self.actionRegistro_indemnizaciones.setObjectName("actionRegistro_indemnizaciones")
        self.actionListado_de_indemnizaciones_abiertas = QtWidgets.QAction(MainWindow)
        self.actionListado_de_indemnizaciones_abiertas.setIcon(icon40)
        self.actionListado_de_indemnizaciones_abiertas.setObjectName("actionListado_de_indemnizaciones_abiertas")
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionImportar_BD)
        self.menuArchivo.addAction(self.actionGuardar_BD_como)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionCerrar)
        self.menuDefiniciones.addAction(self.actionDatos_de_la_sociedad)
        self.menuDefiniciones.addAction(self.actionPeriodos)
        self.menuDefiniciones.addAction(self.actionD_as_No_laborables)
        self.menuDefiniciones.addAction(self.actionDefinir_vacaciones)
        self.menuDefiniciones.addAction(self.actionDefinir_salario_m_nimo)
        self.menuDefiniciones.addAction(self.actionDefinir_tabla_ISLR)
        self.menuDefiniciones.addAction(self.actionListado_de_nacionalidades)
        self.menuDefiniciones.addAction(self.actionConfigurar_correo_de_n_mina)
        self.menuTrabajadores.addAction(self.actionListado_de_trabajadores)
        self.menuHoras_extraordinarias.addAction(self.actionRegistro_de_horas_extra)
        self.menuHoras_extraordinarias.addAction(self.actionListado_de_horas_extra)
        self.menuInasistencias.addAction(self.actionRegistro_de_inasistencia_2)
        self.menuInasistencias.addAction(self.actionListado_de_inasistencias)
        self.menuRegistro_de_comisi_n.addAction(self.actionRegistro_de_comisi_n)
        self.menuRegistro_de_comisi_n.addAction(self.actionListado_de_comisiones)
        self.menuOtras_remuneraciones.addAction(self.actionRegistro_de_otra_remuneraci_n_2)
        self.menuOtras_remuneraciones.addAction(self.actionListado_otras_remun)
        self.menuRemuneraci_n_otros_empleadores.addAction(self.actionRegistro_rem_otro_empleador)
        self.menuRemuneraci_n_otros_empleadores.addAction(self.actionListado_rem_otro_empleador)
        self.menuIndemnizaciones_laborales.addAction(self.actionRegistro_indemnizaciones)
        self.menuIndemnizaciones_laborales.addAction(self.actionListado_de_indemnizaciones_abiertas)
        self.menuVariaciones.addAction(self.menuHoras_extraordinarias.menuAction())
        self.menuVariaciones.addAction(self.menuInasistencias.menuAction())
        self.menuVariaciones.addAction(self.menuRegistro_de_comisi_n.menuAction())
        self.menuVariaciones.addAction(self.menuOtras_remuneraciones.menuAction())
        self.menuVariaciones.addAction(self.menuRemuneraci_n_otros_empleadores.menuAction())
        self.menuVariaciones.addAction(self.menuIndemnizaciones_laborales.menuAction())
        self.menuVariaciones.addAction(self.actionRegistro_de_salario_nuevo)
        self.menuVariaciones.addAction(self.actionRegistro_de_salario_por_lote)
        self.menuVariaciones.addAction(self.actionRegistro_de_pr_stamo_adelanto)
        self.menuVariaciones.addAction(self.actionRegistro_de_dotaci_n)
        self.menuBeneficios.addAction(self.actionCostos_laborales)
        self.menuBeneficios.addAction(self.actionBeneficios_seg_n_ley)
        self.menuN_mina.addAction(self.actionN_mina_quincenal)
        self.menuN_mina.addAction(self.actionN_mina_Individual)
        self.menuN_mina.addAction(self.actionPago_utilidades)
        self.menuN_mina.addAction(self.actionLiquidaci_n)
        self.menuReportes.addAction(self.actionFormato_de_asistencia)
        self.menuReportes.addAction(self.actionInforme_TSS)
        self.menuReportes.addAction(self.actionResumen_de_recibos)
        self.menuReportes.addAction(self.actionCarta_de_trabajo)
        self.menuAyuda.addAction(self.actionContenido_de_la_Ayuda)
        self.menuAyuda.addAction(self.actionAcerca_de_SNP)
        self.menuAyuda.addAction(self.actionHaga_una_donaci_n)
        self.menuCambiar_tema_2.addAction(self.actionClaro)
        self.menuCambiar_tema_2.addAction(self.actionObscuro_2)
        self.menuVentana.addAction(self.actionCascada)
        self.menuVentana.addAction(self.actionMosaico)
        self.menuVentana.addAction(self.actionPantalla_completa)
        self.menuVentana.addAction(self.menuCambiar_tema_2.menuAction())
        self.menuVentana.addSeparator()
        self.menuVentana.addAction(self.actionVer_info)
        self.menuVentana.addSeparator()
        self.menuVentana.addAction(self.actionBloquear)
        self.menuUsuarios.addAction(self.actionListado_de_usuarios)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuDefiniciones.menuAction())
        self.menubar.addAction(self.menuTrabajadores.menuAction())
        self.menubar.addAction(self.menuVariaciones.menuAction())
        self.menubar.addAction(self.menuBeneficios.menuAction())
        self.menubar.addAction(self.menuN_mina.menuAction())
        self.menubar.addAction(self.menuReportes.menuAction())
        self.menubar.addAction(self.menuUsuarios.menuAction())
        self.menubar.addAction(self.menuVentana.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.toolBar.addAction(self.actionPeriodos)
        self.toolBar.addAction(self.actionListado_de_trabajadores)
        self.toolBar.addAction(self.actionN_mina_quincenal)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nomina"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuDefiniciones.setTitle(_translate("MainWindow", "Definiciones"))
        self.menuTrabajadores.setTitle(_translate("MainWindow", "Trabajadores"))
        self.menuVariaciones.setTitle(_translate("MainWindow", "Variaciones"))
        self.menuHoras_extraordinarias.setTitle(_translate("MainWindow", "Horas extraordinarias"))
        self.menuInasistencias.setTitle(_translate("MainWindow", "Inasistencias"))
        self.menuRegistro_de_comisi_n.setTitle(_translate("MainWindow", "Comisiones"))
        self.menuOtras_remuneraciones.setTitle(_translate("MainWindow", "Otras remuneraciones"))
        self.menuRemuneraci_n_otros_empleadores.setTitle(_translate("MainWindow", "Remuneración otros empleadores"))
        self.menuIndemnizaciones_laborales.setTitle(_translate("MainWindow", "Indemnizaciones laborales"))
        self.menuBeneficios.setTitle(_translate("MainWindow", "Beneficios"))
        self.menuN_mina.setTitle(_translate("MainWindow", "Nómina"))
        self.menuReportes.setTitle(_translate("MainWindow", "Reportes"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.menuVentana.setTitle(_translate("MainWindow", "Ventana"))
        self.menuCambiar_tema_2.setTitle(_translate("MainWindow", "Cambiar tema"))
        self.menuUsuarios.setTitle(_translate("MainWindow", "Usuarios"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "Accesos"))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "Info"))
        self.label.setText(_translate("MainWindow", "Cumpleaños\n"
"del mes:"))
        self.label_3.setText(_translate("MainWindow", "Próximo período\n"
"vacacional:"))
        self.label_2.setText(_translate("MainWindow", "Días feriados\n"
"del mes:"))
        self.label_4.setText(_translate("MainWindow", "Estatus de\n"
"trabajadores:"))
        self.actionCerrar.setText(_translate("MainWindow", "Cerrar"))
        self.actionPeriodos.setText(_translate("MainWindow", "Periodos"))
        self.actionD_as_No_laborables.setText(_translate("MainWindow", "Días No laborables"))
        self.actionDefinir_vacaciones.setText(_translate("MainWindow", "Definir vacaciones"))
        self.actionDefinir_salario_m_nimo.setText(_translate("MainWindow", "Definir salario mínimo"))
        self.actionDefinir_tabla_ISLR.setText(_translate("MainWindow", "Definir tabla ISLR"))
        self.actionDefinici_n_de_riesgo_laboral.setText(_translate("MainWindow", "Definir factor de riesgo laboral"))
        self.actionListado_de_trabajadores.setText(_translate("MainWindow", "Listado de trabajadores"))
        self.actionPlano.setText(_translate("MainWindow", "Plano"))
        self.actionObscuro.setText(_translate("MainWindow", "Obscuro"))
        self.actionCascada.setText(_translate("MainWindow", "Cascada"))
        self.actionMosaico.setText(_translate("MainWindow", "Mosaico"))
        self.actionClaro.setText(_translate("MainWindow", "Claro"))
        self.actionObscuro_2.setText(_translate("MainWindow", "Obscuro"))
        self.actionConfigurar_correo_de_n_mina.setText(_translate("MainWindow", "Configurar correo de nómina"))
        self.actionBloquear.setText(_translate("MainWindow", "Bloquear"))
        self.actionRegistro_de_salario_nuevo.setText(_translate("MainWindow", "Registro de salario nuevo"))
        self.actionRegistro_de_dotaci_n.setText(_translate("MainWindow", "Registro de dotación"))
        self.actionCostos_laborales.setText(_translate("MainWindow", "Costos legales parafiscales"))
        self.actionBeneficios_seg_n_ley.setText(_translate("MainWindow", "Beneficios según ley"))
        self.actionN_mina_quincenal.setText(_translate("MainWindow", "Nómina quincenal"))
        self.actionLiquidaci_n.setText(_translate("MainWindow", "Terminación del contrato de trab"))
        self.actionPago_utilidades.setText(_translate("MainWindow", "Nómina part. los beneficios"))
        self.actionN_mina_extraordinaria.setText(_translate("MainWindow", "Nómina extraordinaria"))
        self.actionFormato_de_asistencia.setText(_translate("MainWindow", "Formato de asistencia"))
        self.actionInforme_TSS.setText(_translate("MainWindow", "Informe TSS"))
        self.actionN_mina_Individual.setText(_translate("MainWindow", "Nómina Individual"))
        self.actionVer_info.setText(_translate("MainWindow", "Ver info"))
        self.actionRegistro_de_salario_por_lote.setText(_translate("MainWindow", "Registro de salario por lote"))
        self.actionDatos_de_la_sociedad.setText(_translate("MainWindow", "Datos de la sociedad"))
        self.actionListado_de_usuarios.setText(_translate("MainWindow", "Listado de usuarios"))
        self.actionListado_de_nacionalidades.setText(_translate("MainWindow", "Listado de nacionalidades"))
        self.actionResumen_de_recibos.setText(_translate("MainWindow", "Resumen de recibos"))
        self.actionCarta_de_trabajo.setText(_translate("MainWindow", "Carta de trabajo"))
        self.actionPantalla_completa.setText(_translate("MainWindow", "Pantalla completa"))
        self.actionRegistro_de_pr_stamo_adelanto.setText(_translate("MainWindow", "Registro de préstamo/adelanto"))
        self.actionContenido_de_la_Ayuda.setText(_translate("MainWindow", "Contenido de la Ayuda"))
        self.actionAcerca_de_SNP.setText(_translate("MainWindow", "Acerca de SNP"))
        self.actionHaga_una_donaci_n.setText(_translate("MainWindow", "Por favor haga una donación"))
        self.actionRegistro_de_horas_extra.setText(_translate("MainWindow", "Registro de horas extra"))
        self.actionListado_de_horas_extra.setText(_translate("MainWindow", "Listado de horas extra"))
        self.actionRegistro_de_inasistencia_2.setText(_translate("MainWindow", "Registro de inasistencia"))
        self.actionListado_de_inasistencias.setText(_translate("MainWindow", "Listado de inasistencias"))
        self.actionRegistro_de_comisi_n.setText(_translate("MainWindow", "Registro de comisión"))
        self.actionListado_de_comisiones.setText(_translate("MainWindow", "Listado de comisiones"))
        self.actionRegistro_de_otra_remuneraci_n_2.setText(_translate("MainWindow", "Registro de otra remuneración"))
        self.actionListado_otras_remun.setText(_translate("MainWindow", "Listado otras remun"))
        self.actionRegistro_rem_otro_empleador.setText(_translate("MainWindow", "Registro rem otro empleador"))
        self.actionListado_rem_otro_empleador.setText(_translate("MainWindow", "Listado rem otro empleador"))
        self.actionGuardar_BD_como.setText(_translate("MainWindow", "Guardar base de datos como..."))
        self.actionImportar_BD.setText(_translate("MainWindow", "Importar base de datos..."))
        self.actionRegistro_indemnizaciones.setText(_translate("MainWindow", "Registro de indemnización"))
        self.actionListado_de_indemnizaciones_abiertas.setText(_translate("MainWindow", "Listado de indemnizaciones abiertas"))


import recurso_rc
